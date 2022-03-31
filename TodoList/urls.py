from django.urls import path

from TodoList.views import AddTask, RemoveTask, ResetTodo, TodoList


urlpatterns = [
    path('',TodoList,name='todo-list'),
    path('add',AddTask,name='add-task'),
    path('remove',RemoveTask,name='remove-task'),
    path('reset',ResetTodo,name='reset-task'),
    
]
