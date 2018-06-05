from rest_framework import serializers
from message.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'id',
            'title',
            'date',
            'kindness',
            'testament_full_text',
            'testament_kr_code',
            'start_chapter',
            'start_verse',
            'end_chapter',
            'end_verse',
            'audio_source',
        )
        read_only_fields = (
            'created_at',
            'updated_at',
        )
