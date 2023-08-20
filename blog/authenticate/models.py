from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.text import slugify


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=50,
        unique=True,
        help_text='Введи логин',
        validators=[
            RegexValidator(
                regex=r'^[\w-]+$',
                message='Введи корректный логин. Логин может содержать буквы, цифры и символы -, _.'
            )
        ]
    )
    slug = models.SlugField(unique=True, verbose_name='URL')

    def get_absolute_url(self):
        return f"/profile/{self.slug}/"


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)