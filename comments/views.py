from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Comment
from article.models import Article
from django.contrib.auth.models import User
from .services import fetch_comments_by_article_id
from django.template.loader import render_to_string


@login_required()
def create_comment(request, article_id):
    response = {'success': False, 'comments': []}
    if request.method == 'POST':
        comment = Comment()
        comment.article = Article.objects.get(id=article_id)
        comment.author = User.objects.get(id=request.user.id)
        comment.content = request.POST.get('content')
        comment.save()
        response['success'] = True
        fetched_comments = fetch_comments_by_article_id(request, article_id, 1)
        template_data = {'comments': fetched_comments, 'article_id': article_id}
        response['comments'] = render_to_string('comments/list.html', template_data)
    return JsonResponse(response, content_type='application/json')