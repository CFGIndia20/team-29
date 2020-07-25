from django.contrib import admin
from .models import company_details, skills_required 
# Register your models here.

admin.site.register(company_details)
admin.site.register(skills_required)
