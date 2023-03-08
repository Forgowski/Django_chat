from django.urls import path, include
from . import  views

urlpatterns = [
    path('', views.home, name='home'),
    path("home", views.home, name="home"),
    path('sign-up', views.sign_up, name='sign-up'),
    path('create_post', views.create_post, name='create_post'),
    path("chat", views.chat, name="chat"),
]
