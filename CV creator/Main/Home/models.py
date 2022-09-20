from django.db import models

# Create your models here.
class Emp(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    contact= models.CharField(max_length=30)
    skill = models.TextField(max_length=200)
    experiance = models.CharField(max_length=30)
    hsc = models.IntegerField(max_length=10)
    ssc = models.IntegerField(max_length=10)
    gradue = models.IntegerField(max_length=10)
    hobby = models.TextField(max_length=200)

    def __str__(self):
        return self.name
    





