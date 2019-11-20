from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from webapp.models import Chat, Message
from django.contrib.auth.models import User
from .serializers import ChatSerializer, UserSerializer


class ChatView(APIView):
    def get(self, request):
        chats = Chat.objects.all()
        serializer = ChatSerializer(chats, many=True)
        return Response({"chats": serializer.data})

    def post(self, request):
        chat = request.data.get('chat')
        serializer = ChatSerializer(data=chat)
        if serializer.is_valid(raise_exception=True):
            chat_saved = serializer.save()
            return Response({"success": "Chat '{}' created successfully".format(chat_saved.name)})
        return False

    def put(self, request, pk):
        saved_chat = get_object_or_404(Chat.objects.all(), pk=pk)
        data = request.data.get('chat')
        serializer = ChatSerializer(instance=saved_chat, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            chat_saved = serializer.save()
            return Response({"success": "Chat '{}' updated successfully".format(chat_saved.name)})
        return False

    def delete(self, pk):
        chat = get_object_or_404(Chat.objects.all(), pk=pk)
        chat.delete()
        return Response({"message": "Chat with id `{}` has been deleted.".format(pk)}, status=204)


class UserView(APIView):
    def get(self, request):
        chats = User.objects.all()
        serializer = UserSerializer(chats, many=True)
        return Response({"users": serializer.data})

    def post(self, request):
        chat = request.data.get('user')
        serializer = UserSerializer(data=chat)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
            return Response({"success": "User '{}' created successfully".format(user_saved.username)})
        return False

    def put(self, request, pk):
        saved_user = get_object_or_404(User.objects.all(), pk=pk)
        data = request.data.get('user')
        serializer = UserSerializer(instance=saved_user, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
            return Response({"success": "User '{}' updated successfully".format(user_saved.name)})
        return False

    def delete(self, pk):
        user = get_object_or_404(User.objects.all(), pk=pk)
        user.delete()
        return Response({"message": "User with id `{}` has been deleted.".format(pk)}, status=204)

