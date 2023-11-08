"""
    View functions for the core pages
    @package networktechsolutions
    @author Noel Nagy
    @website: https://github.com/nagynooel
    ©2023 Noel Nagy - All rights reserved.
"""
from django.shortcuts import render, redirect

from . import utils
from .models import Category
import json


# - Views
def index_view(request):
    if not request.session.get("cart", False):
        request.session["cart"] = []
    return render(request, "default/index.html")


def about_us_view(request):
    return render(request, "default/rolunk.html")


def contact_view(request):
    return render(request, "default/kapcsolat.html")


def shop_view(request):

    context = {
        "products": json.loads(utils.get_all_products(["id", "name", "photo", "price"])),
        "categories": utils.get_categories(),
        "selected_category": -1
    }

    return render(request, "default/aruhaz.html", context)

def shop_category_view(request, category: str):
    try:
        category_object = Category.objects.get(name=category)
    except Category.DoesNotExist as e:
        return redirect("shop")

    context = {
        "products": json.loads(utils.get_products_by_category(category_object.name,["id", "name", "photo", "price"])),
        "categories": utils.get_categories(),
        "selected_category": category_object.id
    }

    return render(request, "default/aruhaz.html", context)


def product_view(request, product_name):
    context = {
        "product": utils.get_product(product_name)
    }
    
    return render(request, "default/termek.html", context=context)


def cart_view(request):
    return render(request, "default/kosar.html")


def payment_view(request):
    return render(request, "default/fizetes.html")


def order_status_view(request, order_number):
    context = {
        "order_number": order_number
    }

    return render(request, "default/rendeles-allapota.html", context=context)

# Api
def add_to_cart(request, product_id: int, quantity: int):
    utils.add_product_to_cart(request, product_id, quantity)
    return redirect("shop")