menu = [
    {'title': "Главная", "url_name": 'home', 'id': 0},
    {'title': "О сайте", 'url_name': 'about', 'id': 1},
    #{'title': "Обратная связь", 'url_name': 'contact', 'id': 2},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu

        return context