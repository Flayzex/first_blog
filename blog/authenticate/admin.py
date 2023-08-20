from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
from .forms import CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'is_active']

admin.site.register(CustomUser, CustomUserAdmin)
