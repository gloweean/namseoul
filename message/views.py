from rest_framework import viewsets
from message.models import Message
from message.serializers.message import MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer