from django.urls import path

from Problem.views import Coding, Problems, PythonCompiler


urlpatterns = [
    path('platform',Coding,name="coding"),
    path('',Problems,name='problem'),
    path('compile',PythonCompiler,name='compile')
]
