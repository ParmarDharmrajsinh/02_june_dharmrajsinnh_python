from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.alogin, name='alogin'),
    path('admin_dashboard/', views.dashboard, name='admin_dashboard'),
]
