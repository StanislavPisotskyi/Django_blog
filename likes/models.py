from django.db import models
from article.models import Article
from django.contrib.auth.models import User


class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
