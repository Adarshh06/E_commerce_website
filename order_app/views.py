from django.shortcuts import render, redirect, get_object_or_404
from product_app.models import Product
from .models import CartItem, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.db import transaction

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    else:
        if not request.session.session_key:
            request.session.create()
        cart_item, created = CartItem.objects.get_or_create(session_key=request.session.session_key, product=product)

    cart_item.quantity += 1
    cart_item.save()
    return redirect('order_app:view_cart')

def view_cart(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
    else:
        cart_items = CartItem.objects.filter(session_key=request.session.session_key)
    
    total = sum(item.total_price() for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, "order/cart.html", context)

@login_required
@transaction.atomic
def checkout(request):
    if request.method == "POST":
        address = request.POST.get("address")
        phone = request.POST.get("phone")

        cart_items = CartItem.objects.filter(user=request.user)
        total = sum(item.total_price() for item in cart_items)

        order = Order.objects.create(
            user=request.user,
            total_amount=total,
            address=address,
            phone=phone
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        cart_items.delete()
        return redirect('order_app:order_success', order_id=order.id)

    return render(request, 'order/checkout.html')

def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'checkout/order_success.html', {'order': order})
