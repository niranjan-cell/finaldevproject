from unicodedata import name
from django.urls import path

from Regex.views import Regex


urlpatterns = [
    path('',Regex,name="regex"),
]
