from django.urls import path
from . import views

app_name = 'product_app'

urlpatterns = [
    path('', views.product_list_view, name='product_list'),
    path('<slug:slug>/', views.product_detail_view, name='product_detail'),
]
