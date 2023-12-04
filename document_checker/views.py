from django.shortcuts import render, redirect
from .forms import DocumentUploadForm
from .models import UploadedDocument
import requests
import hashlib
import pytesseract
from PIL import Image
from .ocr_utils import perform_ocr


def upload_document(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_document = form.save()

             # Perform OCR using the provided API or your own implementation
            ocr_result = perform_ocr(uploaded_document.document.path)


            # Perform OCR and save the hash of the OCR result
            uploaded_document.ocr_result_hash = uploaded_document.calculate_ocr_result_hash()
            uploaded_document.save()

            return render(request, 'result.html', {'ocr_result': uploaded_document.ocr_result_hash})
    else:
        form = DocumentUploadForm()
    return render(request, 'upload.html', {'form': form})


def perform_ocr(file_path):
    # Use Tesseract to perform OCR on the image file
    image = Image.open(file_path)
    ocr_result = pytesseract.image_to_string(image)
    return ocr_result


