from django.shortcuts import render

def Calculator(request):
    return render(request,'Calculator/calculator.html')