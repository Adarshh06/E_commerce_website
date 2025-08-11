from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomLoginForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required


# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('account_app:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Allow login with email
            user = authenticate(username=username_or_email, password=password)
            if user is None:
                try:
                    user_obj = CustomUser.objects.get(email=username_or_email)
                    user = authenticate(username=user_obj.username, password=password)
                except CustomUser.DoesNotExist:
                    user = None

            if user:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('product_app:product_list')
            else:
                messages.error(request, "Invalid credentials.")
    else:
        form = CustomLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def guest_login_view(request):
    guest_user = CustomUser.objects.create_user(
        username=f"guest_{CustomUser.objects.count()+1}",
        password=None
    )
    guest_user.is_active = False
    guest_user.save()
    login(request, guest_user, backend='django.contrib.auth.backends.ModelBackend')
    messages.info(request, "You are logged in as a guest.")
    return redirect('product_app:product_list')


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('account_app:login')
