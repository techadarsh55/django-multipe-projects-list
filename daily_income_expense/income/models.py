from csv import field_size_limit
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Income(models.Model):
    income= models.IntegerField()
    income_type = models.CharField(max_length=30)
    income_description = models.CharField(max_length=300)
    income_date = models.DateField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table = 'income'

    def __str__(self):
        return self.name

from django import forms
class IncomeForm(forms.ModelForm):
    class Meta:
        model=Income
        fields="__all__"