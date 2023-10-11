from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class User(AbstractUser):
    # 添加自定义字段
    bio = models.TextField(blank=True)  # 用户简介
    birth_date = models.DateField(null=True, blank=True)  # 用户生日
    avatar = models.ImageField(upload_to='avatars/', blank=True)  # 用户头像
    # custom_groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_set')

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    mobile = models.CharField(max_length=11, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)

    # 添加自定义字段，如手机号、地址等

    def __str__(self):
        return self.user.username


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # 添加购物车的其他字段

    def __str__(self):
        return f"Cart for {self.user.username}"


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    # 添加其他地址相关字段

    def __str__(self):
        return self.address
