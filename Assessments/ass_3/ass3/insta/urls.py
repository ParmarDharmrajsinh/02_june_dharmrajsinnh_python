from django.urls import path
from . import views

app_name = "insta"

urlpatterns = [
    path('', views.home, name='home'),
    path('post/create/', views.create_post, name='create_post'), 
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/<int:id>/like/', views.like_post, name='like_post'),
    path('post/<int:id>/comment/', views.add_comment, name='add_comment'),
    path('comment/<int:id>/delete/', views.delete_comment, name='delete_comment'),
     path('follow/<int:user_id>/', views.follow_toggle, name='follow_toggle'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
     path('post/<int:pk>/like/', views.like_post, name='like'), 
]
