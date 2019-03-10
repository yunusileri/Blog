from django.shortcuts import render, redirect
from .form import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        # username = request.POST['user_name']
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'accounts/form.html', {'forms': form, 'title': 'Giriş Yap'})


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        # user.is_staff=True # Kullanıcının Admin Paneline Girmesine İzin verir
        # user.is_superuser=True
        user.save()
        new_user = authenticate(request, username=user.username, password=user.password)
        login(request, new_user)
        return redirect('home')

    return render(request, 'accounts/form.html', {'forms': form, 'title': 'Üye Ol'})


def logout_view(request):
    logout(request)
    return redirect('home')
