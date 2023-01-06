from django.forms import ModelForm
from django import forms
from .models import Post,Comment, Rating

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title','description','featured_image','category','demo_link','source_link']


class RatingForm(ModelForm):

    class Meta:
        model = Rating
        fields = ['vote']


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content': 'Comment'}
