from pyexpat import model
from wsgiref.validate import validator
from attr import validate
from django.db import models

# Create your models here.
class EmpRegister(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=30)
    Age = models.IntegerField(max_length=10)
    Contact = models.IntegerField(max_length=10)
    city = models.CharField(max_length=20)

    class Meta:
        db_table = "Employee"


class UserData(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.TextField(max_length=100)
    Contact = models.IntegerField(max_length=11)
    city = models.CharField(max_length=20)

    class Meta:
        db_table = "Userdata"

from django.core.exceptions import ValidationError
def validateerror(value):
    if "@gmail.com" in value:
        return value
    else:
        raise ValidationError("this field is only except the gmail mail", validator=[validateerror])


class GmailValid(models.Model):
    gmail = models.CharField(max_length=200)
