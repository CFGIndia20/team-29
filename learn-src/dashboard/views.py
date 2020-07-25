from django.http import HttpResponse
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home/home.html')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
def student_teacher(request):
    return render(request, 'dashboard/student-teacher.html')
