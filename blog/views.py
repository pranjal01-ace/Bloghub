from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from datetime import date
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
# Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        username = request.user.username
        today = date.today()
        return render(request, "blog/dashboard.html", {'username': username, 'today': today})
    else:
        return HttpResponseRedirect("/auth/login/")

# Add Post
@login_required
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
@login_required
def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/all_post.html', {'posts': posts})

# Post Detail
@login_required
def post_detail(request, post_id): 
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/all_details.html', {'post': post})

# View My Details

@login_required
def my_posts(request):
    post=Post.objects.filter(author=request.user).order_by('-created_at')
    
    return render(request,'blog/my_post.html',{'post': post})