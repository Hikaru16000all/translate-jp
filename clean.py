import os
import time
from openai import OpenAI
from tqdm import tqdm

# ================= Configuration =================
DEEPSEEK_API_KEY = "" # replace with your real api key
INPUT_FILE = os.path.expanduser("") # replace with your real api path
OUTPUT_FILE = os.path.expanduser("") # replace with your real api path
CHUNK_MAX_LENGTH = 2000  # Maximum number of characters per text chunk
MAX_RETRIES = 3          # Maximum retry attempts if API call fails
# =================================================

client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

SYSTEM_PROMPT = """You are a senior bilingual editorial expert with 20 years of experience, as well as a light novel formatting specialist.

Your task is to perform **deep denoising** and **layout reconstruction** on the Chinese text below, which was generated through OCR and initial translation.

Please strictly follow these rules:

1. [Core Denoising] Remove all isolated page numbers, headers/footers, copyright notices, and marginal noise (e.g., |, _, ■).
2. [Sentence Reconstruction] Identify sentences broken by page splits and seamlessly merge lines that logically belong to the same sentence, removing unnecessary line breaks.
3. [Formatting Standardization] Reorganize text into natural paragraphs with a blank line between them. Normalize Chinese punctuation.

Output only the cleaned main text. Do NOT include any explanations or extra commentary.
"""

def smart_chunking(text, max_length):
    """
    Smart chunking: try to split at sentence boundaries or double line breaks
    to avoid cutting sentences in half
    """
    paragraphs = text.split('\n')
    chunks = []
    current_chunk = ""
    
    for para in paragraphs:
        if len(current_chunk) + len(para) > max_length and current_chunk:
            chunks.append(current_chunk)
            current_chunk = para + "\n"
        else:
            current_chunk += para + "\n"
            
    if current_chunk.strip():
        chunks.append(current_chunk)
    return chunks

def call_deepseek_with_retry(chunk_text, chunk_index):
    """API call with automatic retry mechanism"""
    for attempt in range(MAX_RETRIES):
        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": f"Please clean the following text:\n\n{chunk_text}"}
                ],
                temperature=0.1,  # Very low temperature to avoid hallucination or creativity
                stream=False
            )
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            wait_time = (attempt + 1) * 3  # Increasing wait time: 3s, 6s, 9s
            print(f"\n[Warning] Chunk {chunk_index} failed ({e}). Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
            
    print(f"\n[Error] Chunk {chunk_index} failed after {MAX_RETRIES} retries. Original text will be preserved.")
    return chunk_text  # Return original text to prevent data loss

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Input file not found: {INPUT_FILE}")
        return

    print("📄 Reading input text...")
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        full_text = f.read()

    print("✂️ Performing smart chunking...")
    chunks = smart_chunking(full_text, CHUNK_MAX_LENGTH)
    print(f"Total chunks to process: {len(chunks)}\n")

    # Clear output file before writing (overwrite mode)
    open(OUTPUT_FILE, 'w', encoding='utf-8').close()

    print("🚀 Sending chunks to DeepSeek for advanced cleaning...")
    for i, chunk in enumerate(tqdm(chunks, desc="Cleaning progress", unit="chunk")):
        if not chunk.strip():
            continue
            
        cleaned_text = call_deepseek_with_retry(chunk, i + 1)
        
        # Append results incrementally to avoid data loss
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f_out:
            f_out.write(cleaned_text + "\n\n")
            
        time.sleep(0.5)  # Throttle requests to avoid hitting API rate limits

    print(f"\n🎉 Done! Cleaned text has been saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
