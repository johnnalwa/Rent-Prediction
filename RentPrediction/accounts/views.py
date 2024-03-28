from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import userForm, UserLoginForm

def register(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')  # Set success message
            return redirect('login')  # Redirect to the login page after successful registration
        else:
            # Report form errors
            errors = form.errors.as_data()
            for field, error in errors.items():
                messages.error(request, f"{field}: {error[0]}")
    else:
        form = userForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('home_page')  # Redirect to the homepage
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def home(request):
    return render(request, 'home.html')