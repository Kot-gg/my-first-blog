from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import get_object_or_404

# Create your views here.

def post_list(requst):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(requst, 'blog/post_list.html', {'posts': posts})

def post_detail(requst, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(requst, 'blog/post_detail.html', {'post':post})