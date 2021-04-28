from django.shortcuts import render, redirect
from .form import CustomCreationForm
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def register_page(request):
    # if request.user.is_authenticated:
    #     messages.info(request, "You are already logged in")
    #     return redirect("/")
    # else:
    form = CustomCreationForm()
    if request.method == "POST":
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "register.html", context)


def login_page(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in")
        return redirect("/")

    if request.method == "POST":
        login_username = request.POST.get("username")
        login_password = request.POST.get("password")
        user = authenticate(request, username=login_username, password=login_password)

        if user is not None:
            login(request, user)
            messages.success(request, "logged in sucessfully")
            return redirect("/")
    return render(request, "login.html")


def logout_page(request):
    logout(request)
    messages.success(request, "logged out successfully")
    return redirect("/")
