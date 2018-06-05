import json

from django.http import JsonResponse
from message.models import Message
from message.serializers.message import MessageSerializer

# Create your views here.


def main_list(request):
    if request.method == 'GET':
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return JsonResponse(json.dumps(serializer.data, ensure_ascii=False), safe=False)