from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=10)
    add = models.TextField(max_length=200)
    city = models.CharField(max_length=20)
    contact = models.IntegerField(max_length=11)

    class Meta:
        db_table ="pitent_appoint"