from unicodedata import name
from django.urls import path

from Dictionary.views import Dictionary

urlpatterns = [
    path('',Dictionary,name='dictionary'),

]
