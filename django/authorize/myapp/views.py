from django.shortcuts import render,redirect
from .forms import *


# Create your views here.

def index(request):
    if request.method == "POST":
        unm = request.POST.get('email')
        pwd = request.POST.get('password')
        user = usersignup.objects.filter(email=unm, password=pwd)
        if user:
            print("login successful")
            return redirect('home')
        else:
            print("login failed")
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        form=signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)
    return render(request, 'signup.html')

def home(request):
    return render(request, 'home.html')