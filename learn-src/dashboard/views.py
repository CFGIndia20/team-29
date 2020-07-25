from django.http import HttpResponse
from django.shortcuts import render, redirect
#from .models import registration_details
# Create your views here.


def home(request):
    return render(request, 'home/home.html')

def studentregistration(request):
    if request.method == 'POST':
        post=Post()
        post.firstname = request.POST.get('firstname')
        post.lname = request.POST.get('lname')
        post.email = request.POST.get('email')
        post.pno = request.POST.get('pno')
        post.save()       
        return render(request, 'posts/create.html')  
    
    else:
        return render(request,'posts/create.html')
