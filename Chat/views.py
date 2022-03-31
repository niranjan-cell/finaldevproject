from django.shortcuts import render
from Chat.models import Thread


def Message(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads
    }
    return render(request,'Chat/message.html',context)