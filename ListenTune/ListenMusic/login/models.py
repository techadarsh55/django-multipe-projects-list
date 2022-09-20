from statistics import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Userinfo(User):
    Age = models.IntegerField()
    Gender = models.CharField(max_length=8)
    Contact = models.IntegerField(max_length=12)

    class Meta:
            db_table = "userinfo"
