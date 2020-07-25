from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.


def home(request):
    return render(request, 'home/home.html')