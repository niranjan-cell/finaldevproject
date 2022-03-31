from unicodedata import name
from django.urls import path

from VideoRecorder.views import VideoRecorder

urlpatterns = [
    path('',VideoRecorder,name="video-recorder"),
]
