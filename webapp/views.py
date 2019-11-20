from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render
from webapp.models import Chat, Message
from datetime import datetime


def index(request):
    title = "Список чатов"
    current_user = request.user
    lastests = {}
    search = request.GET.get('query')

    if current_user.is_authenticated:
        if search:
            chats = current_user.chat_set.filter(name__icontains=search).all()
        else:
            chats = current_user.chat_set.all()
        for chat in chats:
            lastest = chat.message_set.order_by('-created_at')[0]
            lastests[chat.id] = lastest.text
    else:
        chats = []

    context = {'title': title, 'chats': chats, 'lastests': lastests}
    return render(request, 'index.html', context)

@login_required
def chat(request, chat_id):
    current_user = request.user
    chat = Chat.objects.get(id=chat_id)
    title = chat.name
    if request.method == "POST":
        message_text = request.POST.get('message_text')
        print(message_text)
        message = Message(chat=chat, author=current_user, text=message_text, created_at=datetime.now())
        message.save()

    messages = chat.message_set.order_by('created_at')
    context = {'title': title, 'chat': chat, 'messages': messages}
    return render(request, 'chat.html', context)

def logout(request):
    logout(request)
    return False
