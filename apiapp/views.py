from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework import status,viewsets
from rest_framework.response import Response
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class UserView(APIView):
    def post(self,request,*args,**kwargs):
        ser=UserSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"registered"})
        else:
            return Response({"msg":ser.errors},status=status.HTTP_404_NOT_FOUND)

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        # Filter chats to only include those where the user is a participant
        return Chat.objects.filter(participants=self.request.user)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter messages based on the chat ID passed in the URL
        chat_id = self.kwargs.get('chat_id')
        return Message.objects.filter(chat_id=chat_id)

    def get_serializer_context(self):
        # Provide context to the serializer, useful for custom operations
        context = super().get_serializer_context()
        context.update({
            'request': self.request,
        })
        return context

