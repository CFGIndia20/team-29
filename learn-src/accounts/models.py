from django.db import models

class register(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(max_length = 254)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    ssc = models.BooleanField(default=False)
    hsc = models.BooleanField(default=False)