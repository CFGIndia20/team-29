from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from .models import test_questions, test_results
from accounts.models import student_register
import random


# Create your views here.
@login_required
def test(request):
    if request.method == 'GET':
        user = request.user
        if user:
            student = student_register.objects.get(student_id=user)
            if student.hsc:
                questions = test_questions.objects.filter(question_Id = 2)
                return render(request, 'test/test.html', {'questions':questions})
            else:
                questions = test_questions.objects.filter(question_Id = 1)
                return render(request, 'test/test.html', {'questions':questions})


def testSubmit(request):
    if request.method == 'POST':
        user = request.user
        if user:
            student = student_register.objects.get(student_id=user)
            count = 0
            if student.hsc:
                questions = test_questions.objects.filter(question_Id = 2)
                for question in questions:
                    s = question.question
                    temp = request.POST.getlist(s+'[]')
                    if temp[0] == question.ans:
                        count+=1
                count = count*2
                if count > 7:
                    result = test_results.objects.create(
                        student_id = user,
                        marks = count,
                        is_pass = True,
                        is_aboveAvg = True
                    )
                    result.save()
                    student.is_accepted = True
                    student.save()
                elif count >= 4:
                    result = test_results.objects.create(
                        student_id = user,
                        marks = count,
                        is_pass = True,
                        is_aboveAvg = False
                    )
                    result.save()
                    student.is_accepted = True
                    student.save()
                else:
                    result = test_results.objects.create(
                        student_id = user,
                        marks = count,
                        is_pass = False,
                        is_aboveAvg = False
                    )
                    result.save()
            else:
                questions = test_questions.objects.filter(question_Id = 1)
                for question in questions:
                    s = question.question
                    temp = request.POST.getlist(s+'[]')
                    if temp[0] == question.ans:
                        count+=1
                count = count*2
                if count > 7:
                    result = test_results.objects.create(
                        student_id = user,
                        marks = count,
                        is_pass = True,
                        is_aboveAvg = True
                    )
                    result.save()
                    student.is_accepted = True
                    student.save()
                elif count >= 4:
                    result = test_results.objects.create(
                        student_id = user,
                        marks = count,
                        is_pass = True,
                        is_aboveAvg = False
                    )
                    result.save()
                    student.is_accepted = True
                    student.save()
                else:
                    result = test_results.objects.create(
                        student_id = user,
                        marks = count,
                        is_pass = False,
                        is_aboveAvg = False
                    )
                    result.save()
        auth.logout(request)
        return render(request, 'test/results.html', {'marks': count*2, 'user': user.email})