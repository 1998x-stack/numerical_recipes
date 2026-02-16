#!/usr/bin/env python3

import sys
try:
    from PyPDF2 import PdfReader
except ImportError:
    print("PyPDF2 not found")
    sys.exit(1)

def extract_pages(pdf_path, start_page, end_page):
    try:
        reader = PdfReader(pdf_path)
        
        # Extract text from specified pages (0-indexed in PyPDF2)
        extracted_text = ""
        for page_num in range(start_page - 1, min(end_page, len(reader.pages))):
            page = reader.pages[page_num]
            extracted_text += f"\n--- Page {page_num + 1} ---\n"
            extracted_text += page.extract_text()
        
        return extracted_text
    except Exception as e:
        print(f"Error reading PDF: {str(e)}")
        return None

if __name__ == "__main__":
    pdf_file = "numerical_recipes.pdf"
    start_page = 7
    end_page = 12
    
    text = extract_pages(pdf_file, start_page, end_page)
    if text:
        print(text)
    else:
        print("Could not extract text from PDF")