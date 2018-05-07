# Generated by Django 2.0.4 on 2018-05-07 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='강단주제')),
                ('date', models.DateField(blank=True, null=True, verbose_name='날짜')),
                ('testament_full_text', models.CharField(blank=True, max_length=100, null=True, verbose_name='본문전체')),
                ('testament_kr_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='성서 약어')),
                ('start_chapter', models.PositiveIntegerField(blank=True, null=True, verbose_name='시작 장')),
                ('start_verse', models.PositiveIntegerField(blank=True, null=True, verbose_name='시작 절')),
                ('end_chapter', models.PositiveIntegerField(blank=True, null=True, verbose_name='끝 장')),
                ('end_verse', models.PositiveIntegerField(blank=True, null=True, verbose_name='끝 절')),
                ('audio_source', models.TextField(blank=True, null=True, verbose_name='메세지 경로')),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'message',
                'db_table': 'messages',
            },
        ),
    ]
