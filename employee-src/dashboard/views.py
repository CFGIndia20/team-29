from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base/base.html')

def form(request):
    return render(request, 'company_form/form.html')