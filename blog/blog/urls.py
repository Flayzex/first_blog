from django.contrib import admin
from django.urls import path, include

from .settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('articles.urls')),
    path('authenticate/', include('authenticate.urls')),
]

if DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]