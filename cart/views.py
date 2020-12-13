from django.shortcuts import render
from product.models import Product


def cart(request):
    context = {

    }
    return render(request, "pages/cart.html", context)


def cart_by_id(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    context = {
        "product": product,
    }
    return render(request, "pages/cart.html", context)
