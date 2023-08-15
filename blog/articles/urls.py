from django.urls import path

from .views import *

urlpatterns = [
    path('', ArticlesHomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about')
]
