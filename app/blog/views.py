from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def show(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/show.html', {'post': post})


def index_by_tags(request, slug):
    posts = Post.objects.filter(tags__slug=slug)
    return render(request, 'blog/index.html', {'posts': posts})
