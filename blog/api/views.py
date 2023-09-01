from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .permissions import IsOwnerOrReadOnly
from .serializers import ArticlesSerializer
from articles.models import Articles


class ArticlesAPIMixin:
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer


class ArticlesAPIList(ArticlesAPIMixin, generics.ListCreateAPIView):
    pagination_class = PageNumberPagination


class ArticlesAPIUpdate(ArticlesAPIMixin, generics.RetrieveUpdateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)


class ArticlesAPIDestroy(ArticlesAPIMixin, generics.RetrieveDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)