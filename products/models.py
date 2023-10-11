from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    # 其他字段


class Feature(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # 其他字段
