from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .settings import DEBUG
from .yasg import schema_view


urlpatterns = [
    path('admin/', admin.site.urls),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0),  name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),  name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('', include('articles.urls')),
    path('profile/', include('authenticate.urls')),
    path('api/v1/', include('api.urls')),
]

if DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]