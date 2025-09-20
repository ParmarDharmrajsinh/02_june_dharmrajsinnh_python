from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=20)
    email= models.EmailField()
    dob= models.DateField()
    mobile= models.CharField(max_length=10)
    address= models.TextField()
    
