from dataclasses import field
from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class UserRegister(User):
    Age = models.IntegerField()
    Contact = models.IntegerField()
    Country = models.CharField(max_length=30)
    class Meta:
        db_table = 'RegsiterData'
        
        
        