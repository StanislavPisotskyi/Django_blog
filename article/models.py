from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Article(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=datetime.now)
