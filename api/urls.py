from django.urls import path
from django.conf.urls import url
from .views import ChatView

app_name = "articles"

urlpatterns = [
    path('chats/', ChatView.as_view()),
    path('chats/<int:pk>', ChatView.as_view()),
]
