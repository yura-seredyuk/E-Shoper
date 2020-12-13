
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.product, name='product'),
    path('products', views.cart, name='cart'),
    path('<int:product_id>/', views.cart, name='cart')

]
