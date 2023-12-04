# document_checker/templatetags/custom_filters.py
from django import template
import hashlib

register = template.Library()

@register.filter(name='sha256')
def sha256(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()
