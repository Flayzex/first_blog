from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .permissions import IsOwnerOrReadOnly
from .serializers import ArticlesSerializer
from articles.models import Articles
from articles.utils import DataMixin


class ArticlesAPIMixin:
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer


class ArticlesAPIList(ArticlesAPIMixin, generics.ListCreateAPIView):
    pagination_class = PageNumberPagination


class ArticlesAPIUpdate(ArticlesAPIMixin, generics.RetrieveUpdateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)


class ArticlesAPIDestroy(ArticlesAPIMixin, generics.RetrieveDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)


class DocsAPIView(DataMixin, TemplateView):
    template_name = 'api/docs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Документация API")
        return context | c_def