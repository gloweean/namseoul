# Generated by Django 2.0.4 on 2018-11-22 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20181122_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='date_joined',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
