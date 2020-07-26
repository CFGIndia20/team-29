from django.db import models
from accounts.models import MyUser
class course(models.Model):
    course_name = models.CharField(max_length=250)
    courde_desc = models.CharField(max_length=250)

class slots(models.Model):
    slot_name = models.CharField(max_length=250)
    slot_timing = models.CharField(max_length=250)

class batch(models.Model):
    batch_name = models.CharField(max_length=250)
    batch_count = models.IntegerField()
    batch_max_cap = models.IntegerField(default=15)

class batch_student_map(models.Model):
    batch_id = models.ForeignKey(batch, on_delete=models.CASCADE)
    student_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)

class student_slot_preferance(models.Model):
    student_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    selected_slot = models.CharField(max_length=100)
class allotment(models.Model):
    teachers = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    slot = models.ForeignKey(slots,on_delete=models.CASCADE)
    batch = models.ForeignKey(batch, on_delete=models.CASCADE)
