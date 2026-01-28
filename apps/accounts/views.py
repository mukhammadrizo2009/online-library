from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse


def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Bu username band'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        login(request, user)
        return redirect('login')

    return render(request, 'register.html')

def user_login(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('dashboard')

        return render(request, 'login.html', {
            'error': 'Login yoki parol noto‘g‘ri'
        })

    return render(request, 'login.html')

def user_logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('login')
