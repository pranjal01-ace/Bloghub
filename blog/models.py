from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    CATEGORY_CHOICES = (
        ('tech', 'Technology'),
        ('programming', 'Programming'),
        ('ai', 'Artificial Intelligence'),
        ('web', 'Web Development'),
        ('python', 'Python'),
        ('news', 'News'),
        ('tutorial', 'Tutorial'),
        ('tips', 'Tips & Tricks'),
        ('career', 'Career'),
        ('other', 'Other'),
    )

    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    content = RichTextField()

    image = models.ImageField(upload_to='posts/', blank=True, null=True)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='other'
    )

    views = models.PositiveIntegerField(default=0)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    published_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    #Like Model
    
    # models.py
from django.db import models
from django.contrib.auth.models import User

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"