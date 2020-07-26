from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import student_slot_preferance, allotment
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'home/home.html')

@login_required
def dashboard(request):
    user = request.user
    slot = False
    if student_slot_preferance.objects.filter(student_id = user).exists():
        slot = student_slot_preferance.objects.get(student_id = user)
    return render(request, 'dashboard/dashboard.html', {'slot': slot})

def selectSlot(request ,slotname):
    user = request.user
    slot = student_slot_preferance.objects.create(
        student_id = user,
        selected_slot = slotname
    )
    slot.save()
    return redirect('/dashboard')