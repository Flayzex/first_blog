from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'slug', 'email', 'last_login', 'date_joined')
    list_display_links = ('id', 'username')
    search_fields = ('id', 'username')
    list_filter = ('date_joined',)
    readonly_fields = ('last_login', 'date_joined')

admin.site.register(CustomUser, CustomUserAdmin)


admin.site.site_title = 'Админ-панель пользователей'