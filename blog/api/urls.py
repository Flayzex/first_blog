from django.urls import path

from .views import *


urlpatterns = [
    path('articles/', ArticlesAPIList.as_view()),
    path('articles/<int:pk>/', ArticelsAPIUpdate.as_view())
]
