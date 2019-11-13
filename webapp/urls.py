""" Define URL patterns fo webapp """

from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from webapp import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # Chat page
    url(r'^chats/(?P<chat_id>\d+)/$', views.chat, name='chat'),

    # Login page
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name='login'),

    # Logout page
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
