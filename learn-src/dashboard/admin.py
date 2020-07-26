from django.contrib import admin
from . models import course,slots,batch, batch_student_map, student_slot_preferance, allotment
# Register your models here.
admin.site.register(course)
admin.site.register(slots)
admin.site.register(batch)
admin.site.register(batch_student_map)
admin.site.register(student_slot_preferance)
admin.site.register(allotment)