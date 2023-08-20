from django.urls import path

from .views import *

urlpatterns = [
    path('registration/', RegisterUserView.as_view(), name='registration'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),

    path('<slug:user_slug>/', ProfileDetailView.as_view(), name='user-profile')
]
