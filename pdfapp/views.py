import imp
from django.shortcuts import render
from django.http import FileResponse
import os

# Create your views here.
def show_pdf(request):
    filepath = os.path.join('static','sample.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')