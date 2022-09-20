from django.db import models

# Create your models here.

class EmployeeData(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    city = models.CharField(max_length=30)
    join_date = models.DateField()
    Department = models.CharField(max_length=30)
    avtar_url = models.CharField(max_length=500)

    class Meta:
        db_table = 'EmployeeData'

