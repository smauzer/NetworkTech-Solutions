from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

import os

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id} | {self.name}"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField(upload_to="termekek")
    price = models.IntegerField()

    def __str__(self):
        return f"{self.id} | {self.name}"


class Coupon(models.Model):
    code = models.CharField(max_length=10)
    uses = models.IntegerField(default=0) # 0 means unlimited
    expiration_date = models.DateTimeField(blank=True, null=True)
    # Percentage off from the price of all products
    products_precentage_off = models.DecimalField(max_digits=3, decimal_places=0, default=0, validators=PERCENTAGE_VALIDATOR)
    # Percentage off from the shipping price
    shipping_precentage_off = models.DecimalField(max_digits=3, decimal_places=0, default=0, validators=PERCENTAGE_VALIDATOR)


class Order(models.Model):
    # Personal information
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Shipping information
    postal = models.IntegerField()
    city = models.CharField(max_length=35)
    address = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    # Price
    order_price = models.IntegerField()
    shipping_price = models.IntegerField()
    total_price = models.IntegerField()

    def __str__(self):
        return f"{self.id} | {self.email}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    final_price_per_unit = models.IntegerField()