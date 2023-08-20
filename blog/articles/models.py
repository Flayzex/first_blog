from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Articles(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, verbose_name="User's username")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    title = models.CharField(max_length=255, verbose_name="Title")
    description = models.TextField(blank=True, verbose_name="Description")
    content = models.TextField(verbose_name="Text")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Time create")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Time update")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/{self.slug}/"

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-time_create']
