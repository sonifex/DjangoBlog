from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_lists(request):
    posts = Post.objects.all().order_by('published_at')
    return render(request, 'blog/blog_list.html',{'posts': posts})
