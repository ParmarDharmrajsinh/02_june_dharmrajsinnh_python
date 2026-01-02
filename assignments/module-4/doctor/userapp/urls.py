from django.contrib import admin
from django.urls import path,include
from userapp import views

urlpatterns = [
    path('',views.index),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('features/',views.features,name='features'),
    path('about/',views.about,name='signup'),
    path('contact/',views.contact,name='signup'),
    


]