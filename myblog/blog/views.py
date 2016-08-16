from django.shortcuts import render

# Create your views here.

def post_lists(request):
    return render(request, 'blog/blog_list.html',{})
