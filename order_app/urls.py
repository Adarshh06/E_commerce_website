from django.urls import path
from . import views

app_name = 'order_app'

urlpatterns = [
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    # ...other URL patterns...
]