from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog-post-detail', kwargs={'pk': self.pk})

class Comments(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    post = models.ForeignKey(Post, related_name="post_comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_comments", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content