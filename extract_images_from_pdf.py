import fitz  # PyMuPDF
import sys
import os

def extract_images_from_pdf(pdf_path, output_dir="."):
    # Open the PDF file
    doc = fitz.open(pdf_path)
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    extracted_images = []
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        image_list = page.get_images(full=True)
        
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            
            image_filename = f"{base_name}_page{page_num+1}_img{img_index+1}.{image_ext}"
            image_path = os.path.join(output_dir, image_filename)
            
            with open(image_path, "wb") as f:
                f.write(image_bytes)
                
            print(f"Extracted image to: {image_path}")
            extracted_images.append(image_path)
            
    return extracted_images

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_images_from_pdf.py <pdf_file1> <pdf_file2> ...")
        sys.exit(1)
        
    for pdf_file in sys.argv[1:]:
        if os.path.exists(pdf_file):
            print(f"Processing {pdf_file}...")
            extract_images_from_pdf(pdf_file)
        else:
            print(f"File not found: {pdf_file}")
