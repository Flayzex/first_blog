menu = [
    {'title': "Главная страница", "url_name": 'home'},
    {'title': "О нас", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_article'}
    #{'title': "Обратная связь", 'url_name': 'contact', 'id': 2},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu

        return context