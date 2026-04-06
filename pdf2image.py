import os
from pdf2image import convert_from_path

# Configure paths
base_dir = os.path.expanduser("{workdir}") # replace {workdir} with your real path
pdf_dir = os.path.join(base_dir, "pdf")
image_main_dir = os.path.join(base_dir, "images_output")

if not os.path.exists(image_main_dir):
    os.makedirs(image_main_dir)

# Iterate through all PDF files in the pdf folder
for i in range(1, 311):
    file_name = f"{i:03d}.pdf"  # Format as 001.pdf, 002.pdf ...
    pdf_path = os.path.join(pdf_dir, file_name)
    
    if os.path.exists(pdf_path):
        print(f"Processing: {file_name}")
        
        # Create a separate output directory for each PDF
        target_dir = os.path.join(image_main_dir, f"{i:03d}")
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        
        try:
            # Convert PDF to images (dpi=300 is standard for OCR)
            # If memory is limited, you can add thread_count=4 to speed up
            images = convert_from_path(pdf_path, dpi=300)
            
            for j, img in enumerate(images):
                img_name = f"page_{j+1:03d}.jpg"
                img.save(os.path.join(target_dir, img_name), "JPEG")
            
            print(f"Done: {file_name} -> Saved to {target_dir}")
        except Exception as e:
            print(f"Error processing {file_name}: {e}")
    else:
        print(f"Skipped: {file_name} (file not found)")

print("All PDF conversion tasks completed!")
