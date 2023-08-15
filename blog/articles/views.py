from typing import Any, Dict
from django.views.generic import TemplateView
from django.shortcuts import render


# Create your views here.
class ArticlesHomeView(TemplateView):
    template_name = 'articles/articleshome.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = {'title': 'Главная страница'}
        return context | c_def


class AboutView(TemplateView):
    template_name = 'articles/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = {'title': 'О нас'}
        return context | c_def
