from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):

    bulletin_types = {
        (1, '일상생활'),
        (2, '코딩일기'),
        (3, '맛집정보'),
        (4, '기타 등등'),
    }

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    image = models.ImageField(blank=True)
    # bulletin = models.CharField(max_length=100, choices=bulletin_types)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)