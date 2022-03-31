from django.urls import path
from Ascii.views import Ascii

urlpatterns = [
    path('',Ascii,name='ascii')
]
