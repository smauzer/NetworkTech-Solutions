"""
    URL configuration for static pages
    @package networktechsolutions
    @author Noel Nagy
    @website: https://github.com/nagynooel
    ©2023 Noel Nagy - All rights reserved.
"""
from django.urls import path, register_converter
from . import views

from django.conf import settings
from django.conf.urls.static import static

from .converters import NegativeIntConverter

register_converter(NegativeIntConverter, 'negative_int')

urlpatterns = [
    # Views
    path('', views.index_view, name="index"),
    path('rolunk', views.about_us_view, name="about_us"),
    path('kapcsolat', views.contact_view, name="contact"),
    path('aruhaz', views.shop_view, name="shop"),
    path('aruhaz/kategoriak/<str:category>', views.shop_category_view, name="shop_category"),
    path('termekek/<str:product_name>', views.product_view, name="product"),
    path('kosar', views.cart_view, name="cart"),
    path('fizetes', views.payment_view, name="payment"),
    path('rendeles/<int:order_number>', views.order_status_view, name="order_status"),
    # Api
    path('kosar/hozzad/<int:product_id>/<negative_int:quantity>', views.add_to_cart, name="add_to_cart"),
    path('kosar/eltavolit/<int:product_id>', views.remove_from_cart, name="remove_from_cart"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)