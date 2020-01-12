from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login


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
