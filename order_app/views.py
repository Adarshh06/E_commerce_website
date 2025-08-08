from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, Cart, CartItem
from product_app.models import Product

@login_required
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        
        if not created:
            cart_item.quantity += 1
            cart_item.save()
            
        return redirect('product_app:product_list')  # Update this line
    return redirect('product_app:product_list')  # And this line

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.cartitem_set.all()
    total = cart.get_total()
    return render(request, 'order_app/cart.html', {'items': items, 'total': total})

@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    if request.method == 'POST':
        order = Order.objects.create(
            customer_name=request.user.get_full_name(),
            customer_email=request.user.email,
            address=request.POST.get('address'),
            total_amount=cart.get_total()
        )
        # Clear cart after order creation
        cart.cartitem_set.all().delete()
        return redirect('order_detail', order_id=order.id)
    return render(request, 'order_app/checkout.html')
