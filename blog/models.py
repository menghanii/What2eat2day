from django.conf import settings
from django.db import models
from django.utils import timezone



class Post(models.Model):

    bulletin_types = {
        ('1', '신촌 안'),
        ('2', '신촌 밖'),
    }

    menus = {
        ('ko', '한식'),
        ('us', '양식'),
        ('it', '이탈리안'),
        ('ch', '중식'),
        ('jp', '일식'),
        ('bo', '분식'),
        ('cp', '치킨&햄버거'),
        ('nh', '야식'),
        ('et', '기타'),
    }

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    image = models.ImageField(blank=False)
    image_2 = models.ImageField(blank=True)
    image_3 = models.ImageField(blank=True)
    image_4 = models.ImageField(blank=True)
    bulletin = models.CharField(max_length=100, choices=bulletin_types)
    menu = models.CharField(max_length=100, choices=menus)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)