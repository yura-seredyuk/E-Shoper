from django.urls import path, include
from . import views
# from product import views as vs
from product.models import Product

urlpatterns = [
    path('', views.cart, name='cart'),
    path('<int:product_id>/', views.cart_by_id, name='cart_by_id')

]
