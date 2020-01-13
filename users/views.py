from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User


@user_passes_test(lambda u: not u.is_authenticated, login_url='/')
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index_page')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


@user_passes_test(lambda u: not u.is_authenticated, login_url='/')
def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index_page')
            else:
                return redirect('login_page')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


@login_required()
def sign_out(request):
    logout(request)
    return redirect('login_page')


@login_required()
def account_details(request, username):
    user = User.objects.get(username=username)
    return render(request, 'users/account_details.html', {'user': user})