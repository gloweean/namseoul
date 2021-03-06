# Generated by Django 2.0.4 on 2018-04-20 03:47

import common.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testament_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='성서 이름')),
                ('testament_kr_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='성서 약어')),
                ('order', models.IntegerField(blank=True, null=True, validators=[common.models.validate_max_chapter], verbose_name='성서 번호')),
                ('chapter', models.PositiveIntegerField(blank=True, null=True, verbose_name='장')),
                ('verse', models.PositiveIntegerField(blank=True, null=True, verbose_name='절')),
                ('contents', models.TextField(blank=True, null=True, verbose_name='본문')),
                ('total_chapters', models.PositiveIntegerField(blank=True, null=True, verbose_name='성서의 장수')),
                ('total_verses', models.PositiveIntegerField(blank=True, null=True, verbose_name='해당 장의 절수')),
                ('version', models.CharField(blank=True, default='개역개정', max_length=100, null=True, verbose_name='개정종류')),
            ],
            options={
                'verbose_name': 'bible',
                'verbose_name_plural': 'bible',
                'db_table': 'bible',
            },
        ),
    ]
