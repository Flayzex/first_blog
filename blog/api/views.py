from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .serializers import ArticlesSerializer
from articles.models import Articles


class ArticlesAPIList(generics.ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    pagination_class = PageNumberPagination


class ArticlesAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    pagination_class = PageNumberPagination


class ArticlesAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    pagination_class = PageNumberPagination