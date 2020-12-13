from django.shortcuts import render, get_object_or_404
from .models import Product


def cart2(request):
    print("cart ", cart)
    context = {

    }
    return render(request, "pages/cart.html", context)


def cart(request, product_id):
    print("product_id ", product_id)
    product = get_object_or_404(Product, pk=product_id)
    print(product)
    context = {
        "products": product,
    }
    return render(request, "pages/cart.html", context)
