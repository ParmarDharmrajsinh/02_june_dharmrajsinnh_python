from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('author', 'Author'),
        ('reader', 'Reader'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='reader')

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_posts')
    caption = models.TextField()
    image = models.ImageField(upload_to='posts/')

    def __str__(self):
        
        return (self.caption[:50] + '...') if self.caption and len(self.caption) > 50 else (self.caption or f"Post {self.id}")


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Comment by {self.user.username}"
