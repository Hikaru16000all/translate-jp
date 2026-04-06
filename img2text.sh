#!/bin/bash

# Base directories
INPUT_BASE=~/Vtuber/images_output
OUTPUT_BASE=~/Vtuber/ocr_results

# Create main output directory if it does not exist
mkdir -p "$OUTPUT_BASE"

# Loop through folders 001 to 310
for i in $(seq -f "%03g" 1 310); do
    echo "Processing folder: $i"

    INPUT_DIR="$INPUT_BASE/$i"
    OUTPUT_DIR="$OUTPUT_BASE/$i"

    # Check if input directory exists
    if [ -d "$INPUT_DIR" ]; then
        # Create corresponding output directory
        mkdir -p "$OUTPUT_DIR"

        # Run OCR script
        python3 ocr.py \
            --sourcedir "$INPUT_DIR" \
            --output "$OUTPUT_DIR"

        echo "Finished folder: $i"
    else
        echo "Skipped: $i (input directory not found)"
    fi
done

echo "All OCR tasks completed!"
