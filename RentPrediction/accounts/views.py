from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import userForm, UserLoginForm
# prediction/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from sklearn.externals import joblib


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


# Load the trained model
model = joblib.load(
mode
'/house_price_prediction')

@csrf_exempt
def predict_rent(request):
    if request.method == 'POST':
        try:
            # Extract input data from request
            data = json.loads(request.body)
            
# Preprocess input data
            preprocessed_data = preprocess_data(data)
            
# Make prediction using the model
            prediction = model.predict(preprocessed_data)
            
# Return the prediction as JSON response
            return JsonResponse({'prediction': prediction.tolist()})
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'An error occurred while processing the request'}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)