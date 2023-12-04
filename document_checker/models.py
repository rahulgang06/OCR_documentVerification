from django.db import models
from .ocr_utils import perform_ocr
import hashlib

class UploadedDocument(models.Model):
    document = models.FileField(upload_to='documents/')
    ocr_result_hash = models.CharField(max_length=64, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.document and not self.ocr_result_hash:
            # Calculate and save the hash of the initial OCR result
            self.ocr_result_hash = self.calculate_ocr_result_hash()
            self.save()

    def calculate_ocr_result_hash(self):
        # Hash the initial OCR result
        ocr_result = perform_ocr(self.document.path)
        hashed_result = hashlib.sha256(ocr_result.encode('utf-8')).hexdigest()
        return hashed_result
