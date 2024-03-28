from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import userForm, UserLoginForm
import joblib

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
                return redirect('home_page')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})


def home(request):
    return render(request, 'home.html')


def predict_rent(request):
    if request.method == 'POST':
        house_type = request.POST.get('houseType')
        location = request.POST.get('location')

        # Load the trained model
        model = joblib.load('rent_prediction_model.pkl')

        # Perform prediction using the loaded model
        predicted_rent = predict_rent_from_model(model, house_type, location)

        return JsonResponse({'predicted_rent': predicted_rent})

    return render(request, 'rent_prediction_form.html')



def predict_rent_from_model(model, house_type, location):
    # Placeholder logic for returning hardcoded prediction
    if location == "Nairobi":
        if house_type == "singleRoom":
            return "Rent for Single Room in Nairobi is between Ksh. 4000 and Ksh. 6000."
        elif house_type == "bedsitter":
            return "Rent for Bedsitter in Nairobi is between Ksh. 7000 and Ksh. 8000."
        elif house_type == "oneBedroom":
            return "Rent for 1 Bedroom in Nairobi is between Ksh. 9000 and Ksh. 12000."
        elif house_type == "twoBedroom":
            return "Rent for 2 Bedroom in Nairobi is between Ksh. 13000 and Ksh. 16000."
    elif location == "Nakuru":
        if house_type == "singleRoom":
            return "Rent for Single Room in Nakuru is between Ksh. 3000 and Ksh. 5000."
        elif house_type == "bedsitter":
            return "Rent for Bedsitter in Nakuru is between Ksh. 5000 and Ksh. 6000."
        elif house_type == "oneBedroom":
            return "Rent for 1 Bedroom in Nakuru is between Ksh. 6000 and Ksh. 9000."
        elif house_type == "twoBedroom":
            return "Rent for 2 Bedroom in Nakuru is between Ksh. 9500 and Ksh. 12000."
    elif location == "Eldoret":
        if house_type == "singleRoom":
            return "Rent for Single Room in Eldoret is between Ksh. 2500 and Ksh. 4500."
        elif house_type == "bedsitter":
            return "Rent for Bedsitter in Eldoret is between Ksh. 4600 and Ksh. 5600."
        elif house_type == "oneBedroom":
            return "Rent for 1 Bedroom in Eldoret is between Ksh. 6500 and Ksh. 8500."
        elif house_type == "twoBedroom":
            return "Rent for 2 Bedroom in Eldoret is between Ksh. 9000 and Ksh. 11000."
    else:
        return "Invalid location selection."
