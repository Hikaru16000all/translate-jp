import os

# Configure paths
ocr_results_dir = os.path.expanduser("~/Vtuber/ocr_results")
output_file = os.path.expanduser("~/Vtuber/all_vtuber_text_combined.txt")

def merge_txt_files():
    total_merged = 0
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Loop through folders from 001 to 310 to preserve overall order
        for i in range(1, 311):
            folder_id = f"{i:03d}"
            folder_path = os.path.join(ocr_results_dir, folder_id)
            
            if os.path.exists(folder_path):
                print(f"Reading folder: {folder_id}")
                
                # Get all txt files in the folder and sort them
                # (ensures correct order like page_001, page_002, etc.)
                txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
                txt_files.sort()
                
                for txt_file in txt_files:
                    file_path = os.path.join(folder_path, txt_file)
                    
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        
                        # Optionally write file metadata as a separator
                        # (remove this if not needed)
                        # outfile.write(f"\n\n--- [Folder: {folder_id} | File: {txt_file}] ---\n\n")
                        
                        outfile.write(content)
                        # Ensure a newline between pages to avoid text merging
                        outfile.write("\n")
                        total_merged += 1
            else:
                # Skip non-existing folders
                pass

    print(f"\n✅ Merge completed!")
    print(f"Total text files merged: {total_merged}")
    print(f"Combined file saved at: {output_file}")

if __name__ == "__main__":
    merge_txt_files()
