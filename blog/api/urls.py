from django.urls import path

from .views import *


urlpatterns = [
    path('articles/', ArticlesAPIList.as_view()),
    path('articles/<int:pk>/', ArticlesAPIUpdate.as_view()),
    path('articles/delete/<int:pk>/', ArticlesAPIDestroy.as_view()),
    path('docs/', DocsAPIView.as_view(), name='api_docs'),
]
