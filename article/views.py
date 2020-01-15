from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from .models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist


@login_required()
def get_list(request):
    articles_list = Article.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(articles_list, 5)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
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
    if article.author.id != request.user.id:
        return redirect('articles_list_page')
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


@login_required()
def remove(request, article_id):
    article = Article.objects.get(id=article_id)
    if article.author.id == request.user.id and request.method == 'POST':
        article.delete()
    return redirect('articles_list_page')