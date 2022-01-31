from operator import mod
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    sku = models.CharField(max_length=16)
    price = models.IntegerField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.name

