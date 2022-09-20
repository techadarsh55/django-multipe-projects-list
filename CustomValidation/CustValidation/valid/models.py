from pyexpat import model
from tokenize import Name
from django.db import models
from django.core.exceptions import ValidationError

def Namevalid(Name):
    if Name.isalpha():
        return Name
    else:
        raise ValidationError("Please Enter the Name only not allowed digit")
# Create your models here.
class EmpName(models.Model):
    Name = models.CharField(max_length=50,validators=[Namevalid])

    

