from django.contrib import admin
from .models import CartItem, Order

# If you have an OrderItem model, import and register it as well
# from .models import OrderItem

admin.site.register(CartItem)
admin.site.register(Order)
# admin.site.register(OrderItem)  # Uncomment if OrderItem exists
