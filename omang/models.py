from django.db import models

# Create your models here.
class Omang(models.Model):
    ID_Number = models.CharField(max_length=9, unique=True)
    surname = models.CharField(max_length=200)
    forenames = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=200)
    nationality  = models.CharField(max_length=200)
    sex = models.CharField(max_length=10)
    date_of_expiry = models.DateField()
    colour_of_eyes = models.CharField(max_length=200)
    place_of_application =models.CharField(max_length=200)