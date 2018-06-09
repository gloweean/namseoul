from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class MyUser(AbstractUser):
    gender = models.CharField(
        max_length=10,
        choices=settings.GENDER_CHOICE,
        default='OTHER',
    )
    birthday = models.DateField(blank=True, null=True)