from django.urls import path

from .views import ArticlesAPIList


urlpatterns = [
    path('articles/', ArticlesAPIList.as_view()),
]
