from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User


class UserAuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)
