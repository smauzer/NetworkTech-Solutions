"""
    View functions for the core pages
    @package networktechsolutions
    @author Noel Nagy
    @website: https://github.com/nagynooel
    ©2023 Noel Nagy - All rights reserved.
"""
from django.shortcuts import render

# Index page
def index_view(request):
    return render(request, "default/index.html")