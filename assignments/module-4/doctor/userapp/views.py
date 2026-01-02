from django.shortcuts import render,redirect
from .forms import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
     msg=""
     if request.method=='POST':
        email=request.POST['email']
        pas=request.POST['password']
        
        user=usersignup.objects.filter(email=email,password=pas)
        userid=usersignup.objects.get(email=email)
        print(userid.id)
        if user: #TRUE
            print("Login Successfully!")
            msg="Login Successfully!"
            request.session["user"]=email
            request.session["userid"]=userid.id
            
            return redirect('/')
        else:
            print("Error!Login Faild...")
            msg="Error!Login Faild..."
     return render(request,'login.html',{'msg':msg})

def signup(request):
    msg=""
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            msg="signup successfully"
            return redirect('login')
        
        else:
            print(form.errors)
            msg="error! something wrong"
    return render(request,'signup.html',{'msg':msg})


def features(request):
    return render(request,'features.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')