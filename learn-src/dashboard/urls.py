from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('templates/dashboard', views.dashboard, name = 'dashboard'),
    path('dashboard/student_register',views.student_teacher,name = 'student_teacher'),
]