from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Emp(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    contact = models.IntegerField(max_length=11)
    age = models.IntegerField(max_length=5)

class User1(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    contact = models.IntegerField()
