from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'login.html')