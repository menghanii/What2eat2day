from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    real_name = models.CharField(max_length=20)
    # fans = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='stars', blank=True)
