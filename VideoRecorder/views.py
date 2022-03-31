from django.shortcuts import render

def VideoRecorder(request):
    return render(request,'VideoRecorder/video-recorder.html')