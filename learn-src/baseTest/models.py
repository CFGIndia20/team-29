from django.db import models
from accounts.models import MyUser

# Create your models here.

class test_questions(models.Model):
    question_Id = models.IntegerField()
    question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=250)
    option2 = models.CharField(max_length=250)
    option3 = models.CharField(max_length=250)
    option4 = models.CharField(max_length=250)
    ans = models.CharField(max_length=250)


class test_results(models.Model):
    student_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    marks = models.IntegerField()
    is_pass = models.BooleanField(null = True,default=None)
    is_aboveAvg = models.BooleanField(default=False)