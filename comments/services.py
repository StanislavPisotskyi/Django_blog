from .models import Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def fetch_comments_by_article_id(request, article_id, default_page):
    comments_list = Comment.objects.all().filter(article=article_id).order_by('-id')
    page = request.GET.get('page', default_page)
    paginator = Paginator(comments_list, 5)
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    return comments
