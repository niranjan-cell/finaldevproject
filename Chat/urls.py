from unicodedata import name
from django.urls import path

from Chat.views import Message

urlpatterns = [
    path('',Message,name="message"),
]
