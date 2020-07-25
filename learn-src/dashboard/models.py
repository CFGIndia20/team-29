# from django.db import models

class appliedstudent(models.Models):
    ssc = models.BooleanField(default=False)
    hsc = models.BooleanField(default=False)

class slots(models.Model):
    time = models.TimeField()
    slotno = models.IntegerField()

# class teacher(models.Model):
#     qualification = models.CharField(max_length=50)

class allotment(models.Model):
    teachers = models.ForeignKey(teacher,on_delete=models.CASCADE)
    slotno = models.ForeignKey(slots,on_delete=models.CASCADE)
    batchno = models.IntegerField()
