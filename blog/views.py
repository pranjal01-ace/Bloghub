from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from datetime import date
from .models import Post
from .forms import PostForm

# Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        username = request.user.username
        today = date.today()
        return render(request, "blog/dashboard.html", {'username': username, 'today': today})
    else:
        return HttpResponseRedirect("/auth/login/")

# Add Post
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('all_posts')
    else:
        form = PostForm()
    return render(request, "blog/add_post.html", {"form": form})

# All Posts
def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/all_post.html', {'posts': posts})

# Post Detail
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})