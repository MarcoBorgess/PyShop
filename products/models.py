from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)  # 2083 its the max for a URL


class Offer(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=2083)
    discount = models.FloatField()
