import fitz  # PyMuPDF
import argparse
import os
from pathlib import Path
import pytesseract
from PIL import Image
import io

def extract_text_from_pdf(pdf_path, output_path=r"C:\Users\24adi\OneDrive\Desktop\newStuff\Danalysis\RAG_stuff\kk.txt", use_ocr=True):
    """
    Extract text from a PDF file, with OCR support for scanned documents.
    
    Args:
        pdf_path (str): Path to the PDF file
        output_path (str, optional): Path to save the extracted text
        use_ocr (bool): Whether to use OCR if regular extraction fails
    
    Returns:
        str: Extracted text
    """
    try:
        # Open the PDF
        doc = fitz.open(pdf_path)
        
        # Try regular text extraction first
        text = ""
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            page_text = page.get_text()
            text += page_text
        
        # If text extraction yielded very little text and OCR is enabled, use OCR
        if len(text.strip()) < 100 and use_ocr:
            print("Regular text extraction yielded minimal results. Using OCR...")
            text = ""
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                
                # Get page as an image
                pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x zoom for better OCR
                img = Image.open(io.BytesIO(pix.tobytes("png")))
                
                # Use pytesseract to extract text from the image
                page_text = pytesseract.image_to_string(img)
                text += page_text + "\n\n"
                print(f"OCR processed page {page_num+1}/{len(doc)}")
        
        # Close the document
        doc.close()
        
        # Save or return the text
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Text extracted and saved to {output_path}")
        
        return text
        
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None

if __name__ == "__main__":
    # Set up command line arguments
    parser = argparse.ArgumentParser(description='Extract text from a PDF file')
    parser.add_argument('pdf_path', help='Path to the PDF file')
    parser.add_argument('-o', '--output', help='Path to save the extracted text')
    parser.add_argument('--no-ocr', action='store_true', help='Disable OCR for scanned documents')
    args = parser.parse_args()
    
    # Get the PDF path
    pdf_path = args.pdf_path
    
    # Set default output path if not provided
    if not args.output:
        pdf_name = Path(pdf_path).stem
        output_path = f"{pdf_name}_text.txt"
    else:
        output_path = args.output
    
    # Extract text
    extract_text_from_pdf(pdf_path, output_path, use_ocr=not args.no_ocr) 