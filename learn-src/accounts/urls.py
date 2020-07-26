from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('accounts/register', views.register, name = 'register'),
    path('accounts/login', views.login, name = 'login'),
    path('accounts/logout', views.logout, name = 'logout'),
]