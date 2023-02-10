from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login

from . models import *
from . forms import *

# Create your views here.
 
def registerUser(request):
    form = register()

    if request.method == "POST":
        form = register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginPage')

    context = {"form":form}
    return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password=password)

        if user is  not None:
            login(request, user)
            return redirect('profile')  
    context = {}
    return render(request, 'accounts/login.html', context)


def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProfileForm

    return render(request, "accounts/profile.html", {'form':form})