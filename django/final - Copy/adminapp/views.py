from django.shortcuts import render,redirect,get_object_or_404
from finalapp.models import *
import datetime
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def admin_home(request):
    if request.method=='POST':
        un=request.POST["username"]
        pa=request.POST["password"]
        
        if un=="admin" and pa=="tops@123":
            print("Login Success!")
            return redirect("admin_dashboard")
        else:
            print("Error!Login Faild...")
    return render(request,'admin_home.html')

def admin_dashboard(request):
    data=Userinfo.objects.all()
    n_data=mynotes.objects.all()
    n=data.count()
    nd=n_data.count()
    return render(request,'admin_dashboard.html',{'n':n,'nd':nd,'data':data})

def admin_userdata(request):
    data=Userinfo.objects.all()
    return render(request,'admin_userdata.html',{'data':data})

def admin_notesdata(request):
    data=mynotes.objects.all()
    return render(request,'notes_data.html',{'data':data})

def notes_approve(request,id):
    nid=get_object_or_404(mynotes,id=id)
    nid.status='Approved'
    nid.updated_at=datetime.datetime.now()
    nid.save()
    print("Note Approved")

    sub="Your note has been approved"
    msg="Hello,\n\nYour note titled '{}' has been approved by the admin.\n\nThank you for your contribution!\n\nBest regards,\nAdmin Team".format(nid.title)
    from_ID=settings.EMAIL_HOST_USER
    to_ID=[nid.email.email]
    send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
    print("Approval email sent to", nid.email.email)
    return redirect('admin_notesdata')


def notes_reject(request,id):
    nid=get_object_or_404(mynotes,id=id)
    nid.status='rejected'
    nid.updated_at=datetime.datetime.now()
    nid.save()
    print("Note rejected")
    return redirect('admin_notesdata')
