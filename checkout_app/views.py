from django.shortcuts import render, redirect, get_object_or_404
from order_app.models import Order

def checkout_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'Paid'
    order.save()
    return redirect('checkout_app:order_success', order_id=order.id)

def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'checkout/order_success.html', {'order': order})
