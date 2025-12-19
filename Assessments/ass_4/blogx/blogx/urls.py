from django.contrib import admin
from django.urls import path, include
from .views import home
urlpatterns = [
     path('', home), 
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/posts/', include('posts.urls')),
]