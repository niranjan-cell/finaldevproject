from unicodedata import name
from django.urls import path

from WhiteBoard.views import WhiteBoard


urlpatterns = [
    path('',WhiteBoard,name="white-board"),
]
