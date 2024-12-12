from django.shortcuts import render,redirect
from login_app.forms import SignUpForm
from django.http import HttpResponse
from django.contrib import messages
from .models import SignUp
import jwt
from django.urls import reverse 



def sign_up(request):
    if request.method == 'POST':
        form_data = SignUpForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return render (request,'login.html')  
    else:
        form_data = SignUpForm()
    return render(request, 'signup.html', {'form': form_data})


SECRET_KEY = ""


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        try:
            user = SignUp.objects.get(user_name=username, password_one=password)

            # Generate JWT token
            payload = {
                'user_id': user.id,
                'username': user.user_name,
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

            # Create a response object
            response = redirect(reverse('dashboard'))  

            # Set cookies process
            response.set_cookie('username', user.user_name)
            response.set_cookie('token', token)

            return response

        except SignUp.DoesNotExist:
            messages.error(request, "Invalid username or password!") 
            return render(request, 'login.html')


    return render(request, 'login.html')


def dashboard(request):
    # Retrieve data from cookies
    username = request.COOKIES.get('username', 'Guest User')
    token = request.COOKIES.get('token', 'No Token')

    return render(request, 'dashboard.html', {
        'username': username.capitalize(),
        'token': token,
    })

def logout(request):
    response = redirect('signup')
    response.delete_cookie('username')
    response.delete_cookie('token')
    return response



