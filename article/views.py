from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm


@login_required()
def get_list(request):
    return render(request, 'articles/list.html')


@login_required()
def create(request):
    form = ArticleForm()
    return render(request, 'articles/create.html', {'form': form})