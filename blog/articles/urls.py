from django.urls import path

from .views import *

urlpatterns = [
    path('', ArticlesHomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('addarticle/', AddArticleView.as_view(), name='add_article'),
    path('<slug:article_slug>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<slug:article_slug>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    path('<slug:article_slug>/', ArticleDetailView.as_view(), name='article-detail')
]
