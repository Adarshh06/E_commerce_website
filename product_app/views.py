from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'products/product_detail.html', {'product': product})

@login_required(login_url='account_app:login')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Store cart in session
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart

    messages.success(request, f"{product.name} added to cart.")
    return redirect('product_app:product_list')

