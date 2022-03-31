"""DeveloperTool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("Home.urls")),
    path('ascii/',include("Ascii.urls")),
    path('calculator/',include('Calculator.urls')),
    path('dictionary/',include('Dictionary.urls')),
    path('stackoverflow/',include('StackOverFlow.urls')),
    path('voice-recorder/',include('VoiceRecorder.urls')),
    path('video-recorder/',include('VideoRecorder.urls')),
    path('regex/',include('Regex.urls')),
    path('white-board/',include('WhiteBoard.urls')),
    path('compiler/',include('Compiler.urls')),
    path('todo-list/',include('TodoList.urls')),
    path('User/',include('User.urls')),
    path('Quiz/',include('Quiz.urls')),
    path('Chat/',include('Chat.urls')),
    path('coding/',include('Problem.urls')),
        
]
