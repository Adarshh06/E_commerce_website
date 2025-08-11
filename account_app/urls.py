from django.urls import path
from . import views

app_name = 'account_app'  # <-- FIXED: should match your folder and namespace

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('guest-login/', views.guest_login_view, name='guest_login'),
    path('logout/', views.logout_view, name='logout'),
]
