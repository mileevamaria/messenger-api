""" Define URL patterns fo webapp """

from django.conf.urls import url
from webapp import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # Chat page
    url(r'^chats/(?P<chat_id>\d+)/$', views.chat, name='chat'),
]

