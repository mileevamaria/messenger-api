from rest_framework import serializers, fields
from django.contrib.auth.models import User
from webapp.models import Chat
from datetime import datetime


class MemberSerializer(serializers.ModelSerializer):
    users = serializers.CharField(source='username')

    class Meta:
        model = Chat
        fields = ('users', )


class ChatSerializer(serializers.Serializer):
    id = fields.IntegerField()
    name = fields.CharField(max_length=200)
    users = MemberSerializer(many=True, read_only=True)
    created_at = fields.DateTimeField()

    class Meta:
        model = Chat
        fields = ('users', )

    def create(self, validated_data):
        return Chat.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id')
        instance.name = validated_data.get('name')
        instance.users = validated_data.get('users')
        instance.created_at = validated_data.get('created_at')
        instance.save()
        return instance


class UserSerializer(serializers.Serializer):
    id = fields.IntegerField()
    username = fields.CharField(max_length=200)
