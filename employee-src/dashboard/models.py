from django.db import models

class company_details(models.Model):
    company_name = models.CharField(max_length=255)
    contact_email = models.EmailField(max_length=255)
    job_profile =  models.CharField(max_length=255)
    job_description = models.CharField(max_length=1000)

    def __str__(self):
        return self.company_name

class skills_required(models.Model):
    company_id = models.ForeignKey(company_details, on_delete=models.CASCADE)
    skills_required = models.CharField(max_length=255)
