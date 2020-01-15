from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(initial='')
    description = forms.CharField(initial='')
    content = forms.CharField(widget=forms.Textarea, initial='')

    class Meta:
        model = Article
        fields = ['title', 'description', 'content', 'author']
