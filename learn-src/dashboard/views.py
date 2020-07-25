from django.http import HttpResponse
from django.shortcuts import render, redirect

def student_teacher(request):
    return render(request, 'dashboard/student-teacher.html')