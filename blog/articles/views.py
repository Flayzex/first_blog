from django.views.generic import TemplateView

from .utils import DataMixin


# Create your views here.
class ArticlesHomeView(DataMixin, TemplateView):
    template_name = 'articles/articleshome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # c_def = {'title': 'Главная страница', 'menu_id': 0}
        c_def = self.get_user_context(title="Главная страница")
        return context | c_def


class AboutView(DataMixin, TemplateView):
    template_name = 'articles/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="О нас")
        return context | c_def
