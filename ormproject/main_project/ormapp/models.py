from unicodedata import name
from django.db import models

# Create your models here.
class Emp (models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name

class Std(models.Model):
    name=models.CharField(max_length=30)
    