from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from datetime import date
from .models import Post, Category
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

# Dashboard

@staff_member_required
def admin_dashboard(request):

    # DATA
    users = User.objects.all()
    posts = Post.objects.all()
    categories = Category.objects.all()

    # FILTER
    category_id = request.GET.get('category')
    if category_id:
        posts = posts.filter(category_id=category_id)

    # STATS
    total_users = users.count()
    total_posts = posts.count()

    context = {
        'users': users,
        'posts': posts,
        'categories': categories,
        'total_users': total_users,
        'total_posts': total_posts,
    }

    return render(request, 'blog/dashboard.html', context)

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

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Like

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    
    if not created:
        # If already liked, remove the like (toggle)
        like.delete()
    
    return redirect('all_posts') 


# DELETE POST (admin allowed)
@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        post.delete()

    return redirect('dashboard')


# DELETE USER (ONLY SUPERADMIN)
@login_required
def delete_user(request, id):
    if not request.user.is_superuser:
        return redirect('dashboard')

    user = get_object_or_404(User, id=id)

    if user != request.user:
        user.delete()

    return redirect('dashboard')