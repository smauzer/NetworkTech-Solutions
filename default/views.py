"""
    View functions for the core pages
    @package networktechsolutions
    @author Noel Nagy
    @website: https://github.com/nagynooel
    ©2023 Noel Nagy - All rights reserved.
"""
from django.shortcuts import render, redirect, HttpResponse

from . import utils
from .models import Category, OrderItem, Order
import random

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
        "selected_category": -1,
        "items_in_cart": len(utils.get_cart(request))
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
        "selected_category": category_object.id,
        "items_in_cart": len(utils.get_cart(request))
    }

    return render(request, "default/aruhaz.html", context)


def product_view(request, product_name):
    context = {
        "product": utils.get_product(product_name),
        "in_cart": utils.in_cart(request, product_name),
        "items_in_cart": len(utils.get_cart(request))
    }
    
    return render(request, "default/termek.html", context=context)


def cart_view(request):

    context = {
        "cart": utils.get_cart(request),
        "total_price": utils.get_total_price(request)
    }

    return render(request, "default/kosar.html", context=context)


def payment_view(request):
    if request.method == "POST":
        request.session["cart"] = []

        return redirect("order_status", order_number=random.randint(1000,9999))

    #     fname = request.POST.get("fname", None)
    #     lname = request.POST.get("lname", None)
    #     company = request.POST.get("company", None)
    #     taxnumber = request.POST.get("taxnumber", None)
    #     email = request.POST.get("email", None)
    #     phone = request.POST.get("phone", None)

    #     invoice_country = request.POST.get("invoice-country", None)
    #     invoice_postal = request.POST.get("invoice-postal", None)
    #     invoice_city = request.POST.get("invoice-city", None)
    #     invoice_address = request.POST.get("invoice-address", None)

    #     shipping_country = request.POST.get("shipping-country", None)
    #     shipping_postal = request.POST.get("shipping-postal", None)
    #     shipping_city = request.POST.get("shipping-city", None)
    #     shipping_address = request.POST.get("shipping-address", None)
    #     message = request.POST.get("message", None)

    #     card_name = request.POST.get("card-name", None)
    #     card_number = request.POST.get("card-number", None)
    #     card_exp_month = request.POST.get("card-exp-month", None)
    #     card_exp_year = request.POST.get("card-exp-year", None)
    #     card_cvc = request.POST.get("card-cvc", None)

    #     cart = request.session["cart"]

    #     order_price = utils.get_total_price(request)
    #     shipping_price = 0 if shipping_country == "HUN" else 1290

    #     Order.objects.create(
    #         name=fname + " " + lname,
    #         company = company,
    #         taxnumber = taxnumber,
    #         email=email,
    #         phone=phone,
    #         invoice_country = invoice_country,
    #         invoice_postal = invoice_postal,
    #         invoice_city = invoice_city,
    #         invoice_address = invoice_address,
    #         shipping_country = shipping_country,
    #         shipping_postal = shipping_postal,
    #         shipping_city = shipping_city,
    #         shipping_address = shipping_address,
    #         message = message,
    #         order_price = order_price,
    #         shipping_price = shipping_price,
    #         total_price = order_price + shipping_price
    #     )

    context = {
        "cart": utils.get_cart(request),
        "total_price": utils.get_total_price(request)
    }

    return render(request, "default/fizetes.html", context)


def order_status_view(request, order_number):
    context = {
        "order_number": order_number
    }

    return render(request, "default/rendeles-allapota.html", context=context)

# Api
def add_to_cart(request, product_id: int, quantity: int):
    return HttpResponse(utils.add_product_to_cart(request, product_id, int(quantity)))

def remove_from_cart(request, product_id: int):
    return HttpResponse(utils.remove_product_from_cart(request, product_id))

def count_cart_items(request):
    return HttpResponse(len(utils.get_cart(request)))