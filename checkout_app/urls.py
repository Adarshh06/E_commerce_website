from django.urls import path
from . import views

app_name = 'checkout_app'

urlpatterns = [
    path('<int:order_id>/checkout/', views.checkout_view, name='checkout'),
    path('success/<int:order_id>/', views.order_success, name='order_success'),
]