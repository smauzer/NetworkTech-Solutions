"""
    View functions for the core pages
    @package networktechsolutions
    @author Noel Nagy
    @website: https://github.com/nagynooel
    ©2023 Noel Nagy - All rights reserved.
"""
from django.shortcuts import render

from . import utils
import json


# - Views
def index_view(request):
    return render(request, "default/index.html")


def about_us_view(request):
    return render(request, "default/rolunk.html")


def contact_view(request):
    return render(request, "default/kapcsolat.html")


def shop_view(request):

    context = {
        "products": json.loads(utils.get_all_products(["id", "name", "photo", "price"]))
    }

    return render(request, "default/aruhaz.html", context)


def product_view(request, product_name):
    context = {
        "product_name": product_name
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