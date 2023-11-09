from .models import Product, Category

from django.forms.models import model_to_dict


# Format multiple product objects as JSON
def product_objects_to_json(product_objects, fields):
    products_json = ""
    
    for product in product_objects:
        products_json += "{"
        for i, field in enumerate(fields):
            products_json += f"\"{field}\": \"{product[i]}\","
        # Remove last colon
        products_json = products_json[:-1]
        products_json += "},"
    
    products_json = products_json[:-1]
    products_json = "[" + products_json + "]"

    return products_json


# Get all products as JSON
# Specify the fields needed as the argument
def get_all_products(fields: list):
    all_product_objects = Product.objects.all().values_list(*fields)
    
    return product_objects_to_json(all_product_objects, fields)


# Get an individual product info as JSON by name
def get_product(name: str):
    product = Product.objects.get(name=name)
    product_dict = model_to_dict(product)

    # Get category name
    product_dict["category"] = Category.objects.get(id = int(product_dict["category"])).name
    
    # Get path to photo
    product_dict["photo"] = product.photo.url

    return product_dict


def get_products_by_category(category_name: str, fields):
    products = Product.objects.filter(category=Category.objects.get(name=category_name)).values_list(*fields)

    return product_objects_to_json(products, fields)


# Get all category names and ids
def get_categories():
    categories = Category.objects.values()
    return [category for category in categories]


# Add a product to the users cart
def add_product_to_cart(request, product_id, quantity=1):
    # Create cart if it does not exists
    if not request.session.get("cart", False):
        request.session["cart"] = []
    
    # If item already in cart add to the quantity
    cart = request.session["cart"]

    for i, item in enumerate(cart):
        if item["id"] == product_id:
            cart[i]["quantity"] = item["quantity"] + quantity
            request.session["cart"] = cart
            return

    cart.append({"id":product_id, "quantity":quantity})
    request.session["cart"] = cart


# Get all products from the users cart
def get_cart(request):
    cart = request.session.get("cart", False)

    if not cart:
        cart = []
        return cart
    
    products_in_cart = []

    # Get information about the items in the cart
    for product in cart:
        name = Product.objects.get(id=product["id"]).name
        product_info = get_product(name)
        # Add quantity
        product_info["quantity"] = product["quantity"]
        products_in_cart.append(product_info)
    
    return products_in_cart


# Get total price of cart
def get_total_price(request):
    cart = get_cart(request)

    total_price = 0
    for product in cart:
        total_price += int(product["price"]) * int(product["quantity"])
    
    return total_price


# Remove product from cart and return new total price
def remove_product_from_cart(request, id):
    cart = request.session.get("cart", False)

    if not cart:
        return 0
    
    cart = [i for i in cart if not (i['id'] == id)]
    
    request.session["cart"] = cart
    return get_total_price(request)