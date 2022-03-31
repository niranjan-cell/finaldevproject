from django.urls import path

from Compiler.views import Compiler


urlpatterns = [
    path('',Compiler,name="compiler"),
]
