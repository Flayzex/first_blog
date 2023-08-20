from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text='Введи логин',
        validators=[
            RegexValidator(
                regex=r'^[\w-]+$',
                message='Введи корректный логин. Логин может содержать буквы, цифры и символы -, _.'
            )
        ]
    )
