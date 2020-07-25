from django.http import HttpResponse
from django.shortcuts import render, redirect

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')