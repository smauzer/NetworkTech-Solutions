from .models import Product, Category

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
    for i, item in enumerate(request.session["cart"]):
        if item["id"] == product_id:
            request.session["cart"][i]["quantity"] = item["quantity"] + quantity
            return

    request.session["cart"].append({"id":product_id, "quantity":quantity})