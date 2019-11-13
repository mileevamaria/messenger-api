from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from webapp.models import Chat, Message

def index(request):
    title = "Список чатов"
    current_user = request.user
    lastests = {}
    if current_user.is_authenticated:
        chats = current_user.chat_set.all()
        for chat in chats:
            lastest = chat.message_set.order_by('-created_at')[0]
            lastests[chat.id] = lastest.text
    else:
        chats = []
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
