from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages, auth
from django.template.context_processors import csrf

from .forms import LoginForm,RegisterForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login as auth_login

# Create your views here.
def register(request):
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            messages.info(request,"Başarıyla Kayıt oldunuz")
            return redirect("index")
        context = {
            "form": form
        }
        return render(request, "register.html", context)
    else:
        form = RegisterForm()
        context = {
            "form":form
         }
        return render(request,"register.html",context)
    # form = RegisterForm()
    # context = {
    #     "form":form
    # }
    #return render(request,'register.html',context)
def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, "login.html", context)
        messages.success(request, "Giriş Yapıldı.")
        login(request,user)
        return redirect("index")
    return render(request, "login.html", context)
def logoutUser(request):
    logout(request)
    messages.success(request,"Çıkış yapıldı.")
    return redirect("index")