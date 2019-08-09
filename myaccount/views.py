from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['userpwd1'] == request.POST['userpwd2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html',{'error':'Userid has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'],email=request.POST['useremail'],password=request.POST['userpwd1'],first_name=request.POST['userhome'],last_name=request.POST['usersex'])
                auth.login(request, user)
                return redirect('index')
        else:
            return render(request, 'signup.html', {'error':'Passwords must match'})
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['userpassword']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html',{'error':'userid or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
    return render(request, 'login.html')

def mypage(request):
    return render(request, 'mypage.html')