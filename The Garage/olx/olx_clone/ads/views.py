from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from .form import *




from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate,logout
from .form import EmailAuthenticationForm
from django.contrib.auth.views import LoginView

def custom_logout(request):
    logout(request)
    return redirect("/") 

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def tempPage(request):
    return render(request,"Garage_home.html")

def email_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')  # Redirect to your home or login success page
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def home_view(request,category_name="False"):
    print(category_name)
    if category_name =="False":
        categories = Vehicle.objects.all()
    else:
        categories = Vehicle.objects.filter(vehicle_name = category_name)
        
    print(categories)

    return render(request, 'home.html',{"vehicles":categories,"search":category_name})




@login_required(login_url="/login/")
def create_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            # If you want to associate the form with the currently logged-in user
            if request.user.is_authenticated:
                form.instance.user = request.user

            form.save()
            # Redirect to a success page or another view
            return redirect('/')
    else:
        form = VehicleForm()

    return render(request, 'create_ad.html', {'form': form})



def create_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            # Associate the address with the currently logged-in user
            address = form.save(commit=False)
            address.user = request.user  # Assuming the user is authenticated
            address.save()
            return redirect('/')  # Redirect to a success page
    else:
        form = AddressForm()

    return render(request, 'add_adress.html', {'form': form})