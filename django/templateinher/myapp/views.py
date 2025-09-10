from django.shortcuts import render

# Create your views here.
def index(requst):
    return render(requst,'index.html')

def contact(requst):
    return render(requst,'contact.html')
def base(requst):
    return render(requst,'base.html')