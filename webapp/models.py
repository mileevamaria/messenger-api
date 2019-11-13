from django.contrib.auth.models import User
from django.db import models


class Chat(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    id = models.IntegerField(primary_key=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]
