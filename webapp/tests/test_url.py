from django.urls import reverse, resolve
from django.test import Client
from django.contrib.auth.models import User
import pytest

class Test:

    def test_chat_url(self):
        """ Test suggestion url and view"""
        path = reverse('chat', kwargs={'chat_id': 1})
        print(path, resolve(path))
        assert resolve(path).view_name == 'chat'

    @pytest.mark.django_db
    def test_login(self):
        """ Test login process """
        c = Client()
        response = c.post('/login/', {'username': 'test', 'password': '123'})
        assert response.status_code == 200



