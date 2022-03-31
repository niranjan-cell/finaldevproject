from unicodedata import name
from django.urls import path

from StackOverFlow.views import StackOverFlow

urlpatterns = [
    path('',StackOverFlow,name="stackoverflow"),
]
