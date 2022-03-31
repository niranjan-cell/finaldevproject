from unicodedata import name
from django.urls import path

from VoiceRecorder.views import VoiceRecorder


urlpatterns = [
    path('',VoiceRecorder,name="voice-recorder"),
]
