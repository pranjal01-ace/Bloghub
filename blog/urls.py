from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='dashboard'),
    path('add-post/', views.add_post, name='add_post'),
    path('all-posts/', views.all_posts, name='all_posts'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('my_posts/',views.my_posts,name="my_posts"),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('delete-user/<int:id>/', views.delete_user, name='delete_user'),
    path('delete-post/<int:id>/', views.delete_post, name='delete_post'),
]