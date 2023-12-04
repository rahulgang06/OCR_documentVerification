# # document_checker/ocr_utils.py
# import pytesseract
# from PIL import Image

# def perform_ocr(file_path):
#     # Use Tesseract to perform OCR on the image file
#     image = Image.open(file_path)
#     ocr_result = pytesseract.image_to_string(image)

#     return ocr_result
# document_checker/ocr_utils.py
# document_checker/ocr_utils.py
# document_checker/ocr_utils.py
# document_checker/ocr_utils.py
# document_checker/ocr_utils.py
# document_checker/ocr_utils.py
# document_checker/ocr_utils.py
# document_checker/ocr_utils.py
# import pytesseract
# import os
# import subprocess
# from PIL import Image

# def perform_ocr(file_path):
#     if file_path.lower().endswith('.pdf'):
#         # If the file is a PDF, convert it to images using Ghostscript
#         image_paths = convert_pdf_to_images_ghostscript(file_path)
#         ocr_results = [perform_ocr_image(image_path) for image_path in image_paths]
#         return ' '.join(ocr_results)
#     else:
#         # For other image formats, perform OCR directly
#         return perform_ocr_image(file_path)

# def perform_ocr_image(image_path):
#     return pytesseract.image_to_string(Image.open(image_path))

# def convert_pdf_to_images_ghostscript(pdf_path):
#     # Create a directory to store the converted images
#     output_dir = os.path.join(os.path.dirname(pdf_path), 'pdf_images')
#     os.makedirs(output_dir, exist_ok=True)

#     # Use Ghostscript to convert PDF to PNG images
#     subprocess.run(['gs', '-sDEVICE=png16m', '-r300', '-o', f'{output_dir}/output%d.png', pdf_path])

#     # Get the list of generated PNG files
#     png_files = [f for f in os.listdir(output_dir) if f.endswith('.png')]

#     return [os.path.join(output_dir, png_file) for png_file in png_files]

# document_checker/ocr_utils.py
# document_checker/ocr_utils.py
# document_checker/ocr_utils.py
# document_checker/ocr_utils.py
# document_checker/ocr_utils.py

# document_checker/ocr_utils.py
# document_checker/ocr_utils.py
# document_checker/ocr_utils.py
# import pytesseract
# from pdf2image import convert_from_path
# import os

# def perform_ocr(file_path):
#     if file_path.lower().endswith('.pdf'):
#         # If the file is a PDF, convert it to images using pdf2image
#         image_paths = convert_pdf_to_images_pdf2image(file_path)
#         ocr_results = [perform_ocr_image(image_path) for image_path in image_paths]
#         return ' '.join(ocr_results)
#     else:
#         # For other image formats, perform OCR directly
#         return perform_ocr_image(file_path)

# def perform_ocr_image(image_path):
#     return pytesseract.image_to_string(image_path)

# def convert_pdf_to_images_pdf2image(pdf_path):
#     # Use pdf2image to convert PDF to images
#     images = convert_from_path(pdf_path, 300)  # 300 is the DPI (adjust as needed)
    
#     # Create a directory to store the converted images
#     output_dir = os.path.join(os.path.dirname(pdf_path), 'pdf_images')
#     os.makedirs(output_dir, exist_ok=True)

#     # Save images and return the paths
#     image_paths = []
#     for i, image in enumerate(images):
#         image_path = os.path.join(output_dir, f'output_page_{i + 1}.png')
#         image.save(image_path, 'PNG')
#         image_paths.append(image_path)

#     return image_paths
# document_checker/ocr_utils.py
import pytesseract
from pdf2image import convert_from_path
import os

def perform_ocr(file_path):
    if file_path.lower().endswith('.pdf'):
        # If the file is a PDF, convert it to images using pdf2image
        image_paths = convert_pdf_to_images_pdf2image(file_path)
        ocr_results = [perform_ocr_image(image_path) for image_path in image_paths]
        return ' '.join(ocr_results)
    else:
        # For other image formats, perform OCR directly
        return perform_ocr_image(file_path)

def perform_ocr_image(image_path):
    return pytesseract.image_to_string(image_path)

def convert_pdf_to_images_pdf2image(pdf_path):
    # Use pdf2image to convert PDF to images
    images = convert_from_path(pdf_path, 300)  # 300 is the DPI (adjust as needed)
    
    # # Create a directory to store the converted images
    # output_dir = os.path.join(os.path.dirname(pdf_path), 'pdf_images')
    # os.makedirs(output_dir, exist_ok=True)

    # Save images and return the paths
    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join('/', f'output_page_{i + 1}.png')
        image.save(image_path, 'PNG')
        image_paths.append(image_path)

    return image_paths

# document_checker/ocr_utils.py
import pytesseract
from pdf2image import convert_from_path
import os
from PIL import Image
import imagehash

def perform_ocr(file_path):
    if file_path.lower().endswith('.pdf'):
        # If the file is a PDF, convert it to images using pdf2image
        image_paths = convert_pdf_to_images_pdf2image(file_path)
        ocr_results = [perform_ocr_image(image_path) for image_path in image_paths]
        check_image_changes(image_paths)
        return ' '.join(ocr_results)
    else:
        # For other image formats, perform OCR directly
        return perform_ocr_image(file_path)

def perform_ocr_image(image_path):
    return pytesseract.image_to_string(image_path)

def convert_pdf_to_images_pdf2image(pdf_path):
    # Use pdf2image to convert PDF to images
    images = convert_from_path(pdf_path, 300)  # 300 is the DPI (adjust as needed)
    
    # Create a directory to store the converted images
    output_dir = os.path.join(os.path.dirname(pdf_path), 'pdf_images')
    os.makedirs(output_dir, exist_ok=True)

    # Save images and return the paths
    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join(output_dir, f'output_page_{i + 1}.png')
        image.save(image_path, 'PNG')
        image_paths.append(image_path)

    return image_paths

def image_hash(image_path):
    # Calculate hash value of the image
    img = Image.open(image_path)
    return imagehash.average_hash(img)

def check_image_changes(image_paths):
    # Check if any image has changed compared to a reference image
    reference_hash = None

    for i, image_path in enumerate(image_paths):
        current_hash = image_hash(image_path)

        if reference_hash is None:
            reference_hash = current_hash
            continue

        if current_hash != reference_hash:
            print(f"Image {i + 1} has changed.")
            # Add your logic to handle the changed image

# Example usage
pdf_path = '/home/rahul/Project/document_verification/documents/RahuGang_Resume.pdf'
perform_ocr(pdf_path)

