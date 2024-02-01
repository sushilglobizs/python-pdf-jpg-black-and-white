import os
import fitz  # PyMuPDF
from PIL import Image

def pdf_to_jpeg(pdf_path, output_folder, quality=100, resolution=300):
    pdf_document = fitz.open(pdf_path)

    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        image = page.get_pixmap()
        img = Image.frombytes("RGB", [image.width, image.height], image.samples)
        output_path = os.path.join(output_folder, f"page_{page_number + 1}.jpeg")
        img.save(output_path, "JPEG", quality=quality, dpi=(resolution, resolution))

    pdf_document.close()

def create_output_folder(pdf_file_name):
    base_name = os.path.splitext(os.path.basename(pdf_file_name))[0]
    output_folder = f"{base_name}"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    return output_folder

def main():
    # Get file name from user
    pdf_file_name = input("Enter the PDF file name (must be in the same directory as this projcet): ")

    # Create output folder based on PDF file name
    output_folder = create_output_folder(pdf_file_name)

    quality = 100           # 0-100
    resolution = 300        # dpi

    # Convert PDF to JPEG
    pdf_to_jpeg(pdf_file_name, output_folder, quality, resolution)

    print("Conversion complete. JPEG images saved in:", output_folder)

if __name__ == "__main__":
    main()
