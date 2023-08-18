from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, ListView, CreateView

from .utils import DataMixin
from .models import *
from .forms import *


# Create your views here.
class ArticlesHomeView(DataMixin, ListView):
    model = Articles
    template_name = 'articles/articleshome.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return context | c_def


class AboutView(DataMixin, TemplateView):
    template_name = 'articles/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="О нас")
        return context | c_def


class ArticleDetailView(DataMixin, DetailView):
    model = Articles
    template_name = 'articles/article.html'
    slug_url_kwarg = 'article_slug'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['articles'])
        return context | c_def


class AddArticleView(DataMixin, LoginRequiredMixin, CreateView):
    form_class = AddArticleForm
    template_name = 'articles/addarticle.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить статью")
        return context | c_def

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
