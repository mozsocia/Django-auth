from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .decorators import *
from .forms import *
from .models import *
# Create your views here.


def hello_view(request):
    message = "Hello World Django"
    return render(request, 'firstapp/hello.html', {'message': message})


from django.contrib.auth.models import User
from django.shortcuts import render, redirect

@guest_only
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            full_name = form.cleaned_data['full_name']
            age = form.cleaned_data['age']

            # Create a new user
            user = User.objects.create_user(username=username, password=password, email=email)

            # Create a profile for the user
            profile = Profile(user=user, full_name=full_name, age=age)
            profile.save()

            # Redirect to login page or any other page after successful registration
            return redirect('login')


    return render(request, 'signup.html')




@guest_only
def login_user(request):
    error_message = None

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # User credentials are correct, log in the user
                login(request, user)
                # Redirect to a success page or any other page
                return redirect('home')
            else:
                # Invalid credentials, show an error message
                error_message = 'Invalid username or password.'

    return render(request, 'login.html', {'error_message': error_message})