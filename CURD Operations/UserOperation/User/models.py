from django.db import models

# Create your models here.

class Emp(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    contact = models.IntegerField(max_length=11)
    city = models.CharField(max_length=30)
    address = models.TextField(max_length=200)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.name