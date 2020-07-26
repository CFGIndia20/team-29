from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import student_slot_preferance
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'home/home.html')

@login_required
def dashboard(request):
    # user = request.user()
    return render(request, 'dashboard/dashboard.html')

def selectSlot(request ,slotname):
    user = request.user
    slot = student_slot_preferance.objects.create(
        student_id = user,
        selected_slot = slotname
    )
    slot.save()
    return redirect('/dashboard')