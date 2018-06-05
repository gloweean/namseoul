from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    GENDER_CHOICE = (
        ('MALE', '남자'),
        ('FEMALE', '여자'),
        ('OTHER', '기타'),
    )
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICE,
        default='OTHER',
    )
    birthday = models.DateField(blank=True, null=True)
