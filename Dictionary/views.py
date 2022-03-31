from django.shortcuts import render

def Dictionary(request):
    return render(request,'Dictionary/dictionary.html')