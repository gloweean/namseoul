from django.db import models
from common.models import Bible


class Message(models.Model):
    def __str__(self):
        name = '{}_{}_{}_{}'.format(self.date, self.kindness, self.title, self.testament_full_text)
        return name
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='강단주제')
    date = models.DateField(blank=True, null=True, verbose_name='날짜')
    kindness = models.CharField(max_length=100, blank=True, null=True, verbose_name='예배종류')
    
    testament_full_text = models.CharField(max_length=100, blank=True, null=True, verbose_name='본문전체')
    
    testament_kr_code = models.CharField(max_length=50, blank=True, null=True, verbose_name='성서 약어')
    start_chapter = models.PositiveIntegerField(blank=True, null=True, verbose_name='시작 장')
    start_verse = models.PositiveIntegerField(blank=True, null=True, verbose_name='시작 절')
    end_chapter = models.PositiveIntegerField(blank=True, null=True, verbose_name='끝 장')
    end_verse = models.PositiveIntegerField(blank=True, null=True, verbose_name='끝 절')
    
    audio_source = models.TextField(blank=True, null=True, verbose_name='메세지 경로')
    
    created_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    
    class Meta:
        db_table = 'messages'
        verbose_name = 'message'
        verbose_name_plural = verbose_name
