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
    print("product", product)

    request.session['cart_list'].append(product)
    print(request.session['cart_list'])
    context = {
        "products": product,
        "cartList": request.session['cart_list'],
    }
    return render(request, "pages/cart.html", context)
