from django.shortcuts import render
from .forms import UserAuthForm, UserRegisterForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm


def auth_user(request):
    if request.method == 'POST':
        form = UserAuthForm(data=request.POST)
        print(request.POST)
        print(form.is_valid())
        print(form.user_cache)
        print(form)
        print(form.errors.as_data())
        if form.is_valid():
            user = form.get_user()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('profile')
    else:
        form = UserAuthForm()
    return render(request, 'login.html', {"form": form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.clean_password2())
            user.save()
    else:
        form = UserRegisterForm()
    return render(request, 'registration.html', {"form": form})
