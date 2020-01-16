from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Like
from article.models import Article
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


@login_required()
def toggle_like(request, article_id):
    result = {'success': False, 'action': 'none'}
    if request.method == 'POST':
        try:
            like_instance = Like.objects.get(article=article_id, user=request.user.id)
        except ObjectDoesNotExist:
            like_instance = None
        if isinstance(like_instance, Like):
            like_instance.delete()
            result['action'] = 'dislike'
        else:
            like = Like()
            like.article = Article.objects.get(id=article_id)
            like.user = User.objects.get(id=request.user.id)
            like.save()
            result['action'] = 'like'
        result['success'] = True
    return JsonResponse(result, content_type='application/json')
