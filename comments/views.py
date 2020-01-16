from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Comment
from article.models import Article
from django.contrib.auth.models import User


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
    return JsonResponse(response, content_type='application/json')