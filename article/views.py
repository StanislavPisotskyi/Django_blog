from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from .models import Article


@login_required()
def get_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html', {'articles': articles})


@login_required()
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles_list_page')
    else:
        form = ArticleForm()
    return render(request, 'articles/form.html', {'form': form})


@login_required()
def get_one_by_id(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'articles/one.html', {'article': article})


@login_required()
def edit(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article.title = form.cleaned_data['title']
            article.description = form.cleaned_data['description']
            article.content = form.cleaned_data['content']
            article.save()
            return redirect('articles_list_page')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/form.html', {'form': form})