from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from .forms import UserLoginForm

def login_view(request):
    title = "login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid(): 
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("posts:list")

    return render(request, "accounts/login.html",{
        "form":form,
        "title":title
    })

def register_view(request):
    return render(request, "accounts/register.html",{
         
    })

def logout_view(request):
    logout(request)
    return redirect("home")