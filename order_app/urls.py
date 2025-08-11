from django.urls import path
from . import views

app_name = 'order_app'  # This enables namespacing like order_app:order_success

urlpatterns = [
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-success/<int:order_id>/', views.order_success, name='order_success'),
    # ...other URL patterns...
]