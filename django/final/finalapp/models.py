from django.db import models

# Create your models here.

class Userinfo(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

class mynotes(models.Model):
    email=models.ForeignKey(Userinfo,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100)
    desc=models.TextField()
    file=models.FileField(upload_to='NotesFolder')
    category=models.CharField(max_length=100)
    statchoice=[
        ('Approved','Approved'),
        ('Pending','Pending'),
        ('Rejected','Rejected')
    ]
    status=models.CharField(max_length=100,choices=statchoice,default='Pending')
    updated_at=models.DateTimeField(blank=True,null=True)

class Contact(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.TextField()
    

