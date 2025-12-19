from django.urls import path
from . import views

urlpatterns = [
     path('', views.post_list),
    path('create/', views.create_post),
    path('<int:post_id>/like/', views.like_post),
    path('<int:post_id>/comment/', views.add_comment),
     path('<int:post_id>/', views.post_detail),
]
