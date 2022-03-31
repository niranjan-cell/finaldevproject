from django.shortcuts import redirect, render
from TodoList import models
def TodoList(request):
    todo=models.TodoList.objects.filter(user=request.user)
    return render(request,'TodoList/todo-list.html',{'tasks':todo})

def AddTask(request):
    todo=models.TodoList()
    todo.user=request.user
    if len(request.POST.get('task'))==0:
            return redirect('todo-list')

    todo.task=request.POST.get('task')
    todo.save()
    return redirect('todo-list')

def RemoveTask(request):
    id=request.GET.get('id')
    models.TodoList.objects.filter(id=id).delete()
    return redirect('todo-list')

def ResetTodo(request):
    models.TodoList.objects.all().delete()
    return redirect('todo-list')
