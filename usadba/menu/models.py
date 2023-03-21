from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    price = models.IntegerField()

    def __str__(self):
        return self.title