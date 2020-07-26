from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from .models import MyUser, student_register
from baseTest.models import test_results

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
            messages.info(request, 'Registered Successfully! wait for varification thank you!')
            return redirect('/accounts/login')
        else:
            messages.info(request, 'password did not match')
            return redirect('/accounts/register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']

        user = auth.authenticate(email=email, password=password)

        if user is not None and user.is_student:
            student = student_register.objects.get(student_id = user)
            if student.is_validated and student.is_accepted:
                auth.login(request, user)
                return redirect('/')
            elif student.is_validated and not student.is_accepted:
                result = test_results.objects.filter(student_id = user).exists()
                if result == True:
                    res = test_results.objects.get(student_id = user)
                    if res.is_pass == False:
                        messages.info(request, 'YOU did not pass baseline test')
                        return render(request, 'accounts/error.html')
                else:
                    auth.login(request, user)
                    messages.info(request, 'complete the baseline test')
                    return redirect('/baseline/test')
            elif not student.is_validated: 
                messages.info(request, 'you were not validated')
                return render(request, 'accounts/error.html')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('/accounts/login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')