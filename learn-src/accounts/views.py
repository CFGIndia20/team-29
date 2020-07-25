from django.shortcuts import render,redirect
from .models import MyUser, student_register
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        lname = request.POST['lname']
        fname = request.POST['fname']
        email = request.POST['email']
        pno = request.POST['pno']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        HSC = request.POST['HSC']
        SSC = request.POST['SSC']
        print(HSC)
        print(SSC)
        if pass1 == pass2:
            user = MyUser.objects.create(
                email = email,
                first_name = lname,
                last_name = fname,
                is_student = True,
                is_teacher = False,
            )
            user.set_password(pass1)
            user.save()
            student = student_register.objects.create(
                phone = pno,
                ssc = SSC,
                hsc = HSC,
                student_id = user
            )
            student.save()

        else:
            messages.info(request, 'password did not match')
            return redirect('/accounts/register')
    else:
        return render(request, 'accounts/register.html')