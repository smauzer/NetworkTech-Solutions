from .models import Product

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