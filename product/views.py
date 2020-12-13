from django.shortcuts import render, get_object_or_404
from product.models import Product
from .models import Product


def cart(request):
    context = {

    }
    return render(request, "pages/cart.html", context)


def cart_by_id(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product,
    }
    return render(request, "pages/cart.html", context)
