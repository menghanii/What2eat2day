from django.conf import settings
from django.db import models
from django.utils import timezone


# 포스팅 모델

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

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 글쓴이 // Accounts.User랑 ForeignKey
    title = models.CharField(max_length=200) # 포스팅 제목 
    text = models.TextField() # 포스팅 글 내용
    created_date = models.DateTimeField(default=timezone.now) # 포스팅 생성 시간
    image = models.ImageField(blank=False) # image를 최대 4개까지 올릴 수 있게 만드려는 의도 // 따로 4개의 ImageField를 생성한 이유는 좀 더 간편한 관리를 위함임. 
    image_2 = models.ImageField(blank=True)
    image_3 = models.ImageField(blank=True)
    image_4 = models.ImageField(blank=True)
    bulletin = models.CharField(max_length=100, choices=bulletin_types) # 음식점의 위치 별로 포스팅을 불러와야 하기 때문에 필요
    menu = models.CharField(max_length=100, choices=menus) # 음식점의 음식 종류 별로 포스팅을 불러와야 하기 때문에 필요
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    address = models.CharField(max_length=300, blank=True) # 네이버 지도 API를 위해 필요

    def __str__(self):
        return self.title

# 댓글 모델

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Accounts.user와 ForeignKey
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') # 포스팅 모델과 ForeignKey
    content = models.CharField(max_length=200) # 댓글 내용
    created_at = models.DateTimeField(auto_now_add=True) # 댓글 생성시간