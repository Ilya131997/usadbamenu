from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(max_length=255, unique=True)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.title
