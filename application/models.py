from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    image = models.ImageField(null=True, blank=True)


class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField()
    date_created = models.DateField(auto_now_add=True)


class Order(models.Model):
    vehicle = models.CharField(max_length=30, unique=True)
    image = models.ImageField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)


class OrderDetail(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)
