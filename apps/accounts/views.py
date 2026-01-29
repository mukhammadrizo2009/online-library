from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        # 1. Parollar tekshirish
        if password != password2:
            messages.error(request, "Parollar bir xil emas!")
            return redirect("register")

        # 2. Username mavjudmi
        if User.objects.filter(username=username).exists():
            messages.error(request, "Bu username band!")
            return redirect("register")

        # 3. Email mavjudmi
        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu email bilan akkaunt bor!")
            return redirect("register")

        # 4. User yaratish
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.first_name = fullname
        user.save()

        messages.success(request, "Ro‘yxatdan o‘tish muvaffaqiyatli! Endi tizimga kiring.")
        return redirect("login")

    return render(request, "register.html")

def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {
                "error": "Login yoki parol noto‘g‘ri"
            })

    return render(request, "login.html")

def home(request):
    return render(request, "main.html")

def user_logout(request: HttpRequest) -> HttpResponse:
    
    logout(request)
    
    return redirect('login')