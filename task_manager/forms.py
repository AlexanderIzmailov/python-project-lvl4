from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext as _


class MyRegisterUserForm(UserCreationForm):
    username = forms.CharField(label=_('Имя пользователя'), widget=forms.TextInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label=_('Имя'), widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label=_('Фамилия'), widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label=_('Пароль'), widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label=_('Подтверждение пароля'), widget=forms.PasswordInput(attrs={'class': 'form-input'}))


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

