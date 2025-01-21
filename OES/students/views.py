from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name'] 
        email = request.POST['email'] 
        password1 = request.POST['password1'] 
        password2 = request.POST['password2'] 
        username = request.POST['username']
        profile_picture = request.FILES.get('profile_picture')
        if User.objects.filter(email=email).exists():
           messages.success(request, 'email already taken')
           redirect('register') 
        elif password1 != password2:
            messages.success(request, 'password do not match')
            redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.success('username already taken')
            redirect('register') 
        else:
            user = User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
            Profile.objects.create(user=user, profile_image=profile_picture)
            # Profile.save()
            user.save()
            messages.success(request, 'successfully registered login here')
            redirect('signin')
    return render(request, 'students/register.html', {})
def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        if email and password1:
            user = authenticate(email=email, password=password1)
            if user is not None:
                login(request, user)
            return redirect('home')
    else:
        messages.success(request, 'incorrect credentials')
        redirect('signin')
    return render(request, 'students/login.html', {})
@login_required
def signout(request):
    logout(request)
    return redirect('signin')
def home(request):
    return render(request, 'students/home.html', {})
@login_required
def profile(request):
    return render(request, 'students/profile.html', {})