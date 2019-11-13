from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from webapp.models import Chat, Message

def index(request):
    title = "Список чатов"
    chats = Chat.objects.all()
    lastests = {}
    for chat in chats:
        lastest = chat.message_set.order_by('-created_at')[0]
        lastests[chat.id] = lastest.text
    context = {'title': title, 'chats': chats, 'lastests': lastests}
    return render(request, 'index.html', context)

def chat(request, chat_id):
    chat = Chat.objects.get(id=chat_id)
    title = chat.name
    messages = chat.message_set.order_by('created_at')
    context = {'title': title, 'chat': chat, 'messages': messages}
    return render(request, 'chat.html', context)

def logout(request):
    logout(request)
    return False
