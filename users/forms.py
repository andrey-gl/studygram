from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User


class UserAuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

