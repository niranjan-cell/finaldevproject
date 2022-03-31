import sys
from django.contrib import messages
from django.shortcuts import render

from Problem.models import Problem

def Problems(request):
    problems = Problem.objects.all()
    return render(request,'Problem/problems.html',{'problems':problems})
def Coding(request):
    id=request.POST.get('id')
    problem=Problem.objects.get(id=id)
    return render(request,'Problem/platform.html',{'problem':problem})

def PythonCompiler(request):
    code=request.POST.get('code')
    problem = Problem.objects.get(id=request.POST.get('id'))
    code = code + '\nsolution("'+ problem.input +'")'
    print(code)
    try:
        original_stdout = sys.stdout
        sys.stdout = open('code.txt','w')
        exec(code)
        sys.stdout.close()
        sys.stdout = original_stdout
        output = open('code.txt','r').read()
    
    except Exception as e:
        sys.stdout = original_stdout
        output = e
    try:
        output = output[:-1]
    except TypeError:
        pass
    if output == problem.output:
        messages.success(request,'Successfully passed the testcases')
        return render(request,'Problem/platform.html',{'problem':problem})

    else:
        return render(request,'Problem/platform.html',{'problem':problem,'output':output})
    