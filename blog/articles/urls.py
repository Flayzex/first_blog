from django.urls import path

from .views import *

urlpatterns = [
    path('', ArticlesHomeView.as_view(), name='home'),
]
