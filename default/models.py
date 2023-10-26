from django.db import models
from django.conf import settings

import os

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT, "termekek"))
    price = models.IntegerField()