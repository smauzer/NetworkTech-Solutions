from .models import Product, Category
from django.core import serializers
import json

from django.forms.models import model_to_dict

# Get all products as JSON
# Specify the fields needed as the argument
def get_all_products(fields: list):
    all_product_objects = Product.objects.all().values_list(*fields)
    
    all_products_json = ""
    
    for product in all_product_objects:
        all_products_json += "{"
        for i, field in enumerate(fields):
            all_products_json += f"\"{field}\": \"{product[i]}\","
        # Remove last colon
        all_products_json = all_products_json[:-1]
        all_products_json += "},"
    
    all_products_json = all_products_json[:-1]
    all_products_json = "[" + all_products_json + "]"
    
    return all_products_json


# Get an individual product info as JSON by name
def get_product(name: str):
    product = Product.objects.get(name=name)
    product_dict = model_to_dict(product)

    # Get category name
    product_dict["category"] = Category.objects.get(id = int(product_dict["category"])).name
    
    # Get path to photo
    product_dict["photo"] = product.photo.url

    return product_dict