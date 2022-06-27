from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone


# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)


def blog_single(request, pid):
    post = get_object_or_404(Post, id=pid, status=1, published_date__lte=timezone.now())
    increment_views(pid)
    context = {"post": post}
    return render(request, "blog/blog-single.html", context)


def increment_views(pid):
    post = get_object_or_404(Post, id=pid)
    post.counted_views += 1
    post.save()


# Defining a function to get previous and next posts of a post in blog
def get_previous_next_posts(pid):
    post = get_object_or_404(Post, id=pid)
    previous_post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date').filter(
        published_date__lte=post.published_date).exclude(id=pid).first()
    next_post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date').filter(
        published_date__gte=post.published_date).exclude(id=pid).last()
    return previous_post, next_post
