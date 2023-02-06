from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, "post/home.html", {"posts": posts})


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "post/detail.html", {"post": post})
