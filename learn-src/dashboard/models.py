from django.db import models

class slots(models.Model):
    time = models.TimeField()
    slotno = models.IntegerField()

class teacher(models.Model):
    qualification = models.CharField(max_length=50)

class allotment(models.Model):
    teachers = models.ForeignKey('',on_delete=models.CASCADE)