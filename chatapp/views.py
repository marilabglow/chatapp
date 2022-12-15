from chatapp.models import Message,UserProfile
from chatapp.serializers import UserSerializer,MessageSerializer
from rest_framework import generics


class user_list(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class user_det(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
class message_list(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    def perform_create(self, serializer):
        user = self.request.user
        print(user.id)
        serializer.save(sender_id=user.id)


class message_det(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    