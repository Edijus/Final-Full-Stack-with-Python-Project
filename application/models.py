from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    image = models.ImageField(null=True, blank=True)


class Categories(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    date_created = models.DateField(auto_now_add=True)


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    text = models.TextField()
    date_created = models.DateField(auto_now_add=True, null=False)

    def __str__(self):
        return f'({self.name})'


""""
class OrderDetail(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)
"""
