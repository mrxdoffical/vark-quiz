from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'accounts/login.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have logged out!')
    else:
        messages.info(request, 'You are not logged in')
    return redirect('home')