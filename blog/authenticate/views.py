from django.contrib.auth import login,logout
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .forms import *
from articles.utils import *


class RegisterUserView(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'authenticate/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return context | c_def

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUserView(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'authenticate/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Войти")
        return context | c_def

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')