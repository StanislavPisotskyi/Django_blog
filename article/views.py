from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm


@login_required()
def get_list(request):
    return render(request, 'articles/list.html')


@login_required()
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles_list_page')
    else:
        form = ArticleForm()
    return render(request, 'articles/create.html', {'form': form})