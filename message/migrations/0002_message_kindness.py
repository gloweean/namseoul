# Generated by Django 2.0.4 on 2018-05-07 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='kindness',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='예배종류'),
        ),
    ]