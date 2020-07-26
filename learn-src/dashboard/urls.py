from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('slot/select/<slotname>', views.selectSlot, name = 'select slot'),
]
