from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm


# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')  # Redirect to login or any other page after registration
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:  # make sure both are filled
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('product_list')  # change if needed
            else:
                return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})
        else:
            return render(request, 'accounts/login.html', {'error': 'Please fill all fields'})
    
    # Always return something for GET requests
    return render(request, 'accounts/login.html')  # Render the login page if GET request.

def logout_view(request):
  logout(request)  # Log out the user. 
  return redirect('login')  # Redirect to the login page after logout.
  
  
def home_view(request):
    return render(request, 'accounts/home.html')  # Render a home page after login.
  

def guest_view(request):
   return redirect('product_list')  # Redirect to product list if the user is not authenticated.
   return render(request, 'accounts/guest.html')  # Render a guest view page.
