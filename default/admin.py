from django.contrib import admin
from .models import Category, Product, Coupon, Order, OrderItem

# Model admin objects
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'price')

class CouponAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'uses', 'expiration_date', 'products_precentage_off', 'shipping_precentage_off')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'order_price', 'shipping_price', 'total_price')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'final_price_per_unit')


# Register models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)