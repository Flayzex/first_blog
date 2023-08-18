from django import forms

from .models import *


class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'slug', 'description', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL статьи'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст'}),
        }