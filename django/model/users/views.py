from django.shortcuts import render, redirect
from .forms import UsersForm

from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = UsersForm()

    return render(request, "register.html", {"form": form})


def common_login(request):
    if request.method == "POST":
        # 입력값 가지고 오기
        username = request.POST.get("username")
        password = request.POST.get("password")
        # db 확인작업 있으면 값을 반환
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # 세션에 담는 작업
            return redirect("index")

    return render(request, "login.html")


def common_logout(request):
    logout(request)
