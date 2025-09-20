from django.shortcuts import render,redirect
from.forms import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = student(request.POST)
        if form.is_valid():
            form.save()
            print("record inserted")
        else:
            print(form.errors)
    else:
        form = student()

    return render(request, 'index.html', {'form': form})
def showdata(request):
    data=product.objects.all()
    print(data)
    return render(request,'showdata.html',{'data':data})


def update(request,id):
    data=product.objects.get(id=id)
    if request.method=='POST':
        form=student(request.POST,instance=data)
        if form.is_valid():
            form.save()
            print("record updated")
            return redirect('showdata')
        else:
            print(form.errors)
    return render(request,'update.html',{'data':data})
    
    
def delete(request,id):
    data=product.objects.get(id=id)
    data.delete(data)
    return redirect('showdata')


