from django.shortcuts import render

def VoiceRecorder(request):
    return render(request,'VoiceRecorder/voice-recorder.html')