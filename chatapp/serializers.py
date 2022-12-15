from django.contrib.auth.models import User
from rest_framework import serializers
from chatapp.models import Message

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    online = serializers.ReadOnlyField(source='userprofile.online')

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'online']


# Message Serializer
class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']
        read_only_fields = ['sender',]