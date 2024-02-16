from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)    
            return redirect('/')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    return render(request, 'login.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password') 

        # Check if passwords match
        if password != re_password:
            return render(request, 'register.html', {'error_message': 'Passwords do not match'})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        return redirect('user-login')
    return render(request, 'register.html')

@login_required(login_url='/account/login')
def homepage(request):
    context = {}
    return render(request, 'homepage.html', context)