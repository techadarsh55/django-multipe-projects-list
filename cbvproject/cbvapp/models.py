
from django.db import models

# Create your models here.

class Emp(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    contact = models.IntegerField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.TextField(max_length=300)
    


from django import forms

class EmpFrom(forms.ModelForm):
    class Meta:
        model = Emp
        fields = "__all__"

