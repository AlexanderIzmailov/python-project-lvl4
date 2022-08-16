import re
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from .forms import *
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.messages.views import SuccessMessageMixin


def base(request):
    return render(request, 'base.html', context={})


# def users(request):
#     users_list = User.objects.all()
#     return render(request, 'users.html', context={
#         'users_list': users_list,
#     })


class Users(ListView):
    model = User
    template_name = "users.html"


class UsersCreate(SuccessMessageMixin, CreateView):
    form_class = MyRegisterUserForm
    template_name = "register.html"
    success_url = reverse_lazy('user_login')
    success_message = _('Учетная запись создана!')


class UsersDetail(DetailView):
    model = User
    template_name = 'users_details.html'
    context_object_name = 'user_details'


class UpdateUser(SuccessMessageMixin, UpdateView):
    model = User
    form_class = MyRegisterUserForm
    template_name = "register.html"
    success_url = reverse_lazy('users_list')
    success_message = _('Учетная запись изменена!')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or self.get_object().pk is not request.user.id and not request.user.is_superuser:
            # return HttpResponse("Permission's error")
            messages.error(request, _("У вас нет прав для изменения другого пользователя"))
            return redirect('users_list')
        return super().dispatch(request, *args, **kwargs)


class DeleteUser(DeleteView):
    model = User
    template_name = "users_delete.html"
    success_url = reverse_lazy('users_list')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or self.get_object().pk is not request.user.id and not request.user.is_superuser:
            # return HttpResponse("Permission's error")
            messages.error(request, _("У вас нет прав для изменения другого пользователя"))
            return redirect('users_list')
        return super().dispatch(request, *args, **kwargs)



class TestPage(TemplateView):
    template_name = "test.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['aaa'] = 'Privet!'
        context['aaa'] = self.request.user.id
        return context


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"

    def get_success_url(self) -> str:
        messages.success(self.request, _("Вы авторизованы!"))
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    messages.success(request, _("Вы вышли!"))
    return redirect('users_list')

