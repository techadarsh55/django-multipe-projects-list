from pyexpat import model
from django.db import models

# Create your models here.
class UserDetail(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    contact = models.IntegerField()
    city = models.CharField(max_length=20)
    salary = models.IntegerField()
    