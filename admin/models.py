from django.db import models
from user.models import User


class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 用户信息字段


class Updates(models.Model):
    # 系统更新字段
    pass


class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 密码重置字段
