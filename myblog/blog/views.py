from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404


# Create your views here.

def post_lists(request):
    posts = Post.objects.all().order_by('published_at')
    return render(request, 'blog/blog_list.html',{'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html',{'post': post})
