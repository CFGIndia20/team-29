from django.db import models

class subjectmarks(models.Models):
    subjectname = models.CharField(max_length=20)
    subjectmarks = models.IntergerField()