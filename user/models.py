from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # 添加自定义字段
    bio = models.TextField(blank=True)  # 用户简介
    birth_date = models.DateField(null=True, blank=True)  # 用户生日
    avatar = models.ImageField(upload_to='avatars/', blank=True)  # 用户头像

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=11, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    # 添加自定义字段，如手机号、地址等

    def __str__(self):
        return self.user.username
