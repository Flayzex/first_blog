menu = [
    {'title': "Главная страница", "url_name": 'home'},
    {'title': "О нас", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_article'}
    #{'title': "Обратная связь", 'url_name': 'contact', 'id': 2},
]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop()

        context['menu'] = user_menu

        return context