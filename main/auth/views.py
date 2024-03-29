from django.shortcuts import render, redirect
from main import models
from django.contrib.auth import authenticate, login, logout



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        if password == password_confirm:
            models.User.objects.create_user(
                username=username,
                password=password
            )
            return redirect('dashboard:log_in')
    return render(request, 'dashboard/auth/register.html')


def log_in(request):
    if request.method =='POST':
        username = request.POST.get(username)
        password = request.POST.get(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:index')
    return render(request, 'dashboard/auth/login.html')


def log_out(request):
    logout(request)
    return redirect('main:index')