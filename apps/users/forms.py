from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'display_name', 'bio', 'avatar', 'password1', 'password2']
        labels = {
            'username': 'Имя пользователя',
            'display_name': 'Никнейм',
            'bio': 'О себе',
            'avatar': 'Фотография',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
        }

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'display_name', 'bio', 'avatar']
        labels = {
            'username': 'Имя пользователя',
            'display_name': 'Никнейм',
            'bio': 'О себе',
            'avatar': 'Фотография',
        }
