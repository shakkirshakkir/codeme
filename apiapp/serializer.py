from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email']
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    class Meta:
        model = Message
        fields = ['id', 'sender', 'content', 'timestamp', 'is_read']

class ChatSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Chat
        fields = ['id', 'participants', 'messages', 'created_at']
