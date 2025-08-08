from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.

def product_list_view(request):
  products = Product.objects.all()
  return render(request, 'products/product_list.html', {'products': products})

def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'products/product_detail.html', {'product': product})
  
