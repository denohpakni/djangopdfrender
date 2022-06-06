from django.urls import path
from pdfapp import views

urlpatterns = [
    path('', views.show_pdf, name="show_pdf"),
]
