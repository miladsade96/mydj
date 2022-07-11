from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import CommentForm
from django.contrib import messages


# Create your views here.
def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')
    if kwargs.get("cat_name") is not None:
        posts = posts.filter(category__name=kwargs["cat_name"], status=1)
    if kwargs.get("author_username") is not None:
        posts = posts.filter(author__username=kwargs["author_username"], status=1)
    if kwargs.get("tag_name") is not None:
        posts = posts.filter(tags__name__in=[kwargs["tag_name"]])

    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get("page")
        posts = posts.page(page_number)
    except PageNotAnInteger:
        posts = posts.page(1)
    except EmptyPage:
        posts = posts.page(1)
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)


def blog_single(request, pid):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post = get_object_or_404(Post, id=pid)
            new_form.save()
            messages.add_message(request, messages.SUCCESS, "Comment added successfully")
        else:
            messages.add_message(request, messages.ERROR, "Error adding comment")
    post = get_object_or_404(Post, id=pid, status=1, published_date__lte=timezone.now())
    comments = Comment.objects.filter(post=post.id, is_approved=True)
    increment_views(pid)
    form = CommentForm()
    context = {"post": post, "comments": comments, "form": form}
    previous_post, next_post = get_previous_next_posts(pid)
    if previous_post:
        context["previous_post"] = previous_post
    if next_post:
        context["next_post"] = next_post
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


def blog_search(request):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')
    if request.method == "GET":
        if s := request.GET.get("s"):
            posts = posts.filter(content__icontains=s)
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)
