from unicodedata import name
from django.urls import path

from Calculator.views import Calculator

urlpatterns = [
    path('',Calculator,name="calculator"),
]
