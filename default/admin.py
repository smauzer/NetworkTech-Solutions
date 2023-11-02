from django.contrib import admin
from .models import Category, Product, Coupon, Order, OrderItem

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Coupon)
admin.site.register(Order)
admin.site.register(OrderItem)