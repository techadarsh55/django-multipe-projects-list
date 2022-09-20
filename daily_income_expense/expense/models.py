from tkinter import CASCADE
from django.db import models
from user.views import User
# Create your models here.

class Expense(models.Model):
    expense= models.IntegerField()
    exp_type = models.CharField(max_length=30)
    exp_description = models.CharField(max_length=300)
    exp_date = models.DateField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table = 'expense'

    def __str__(self):
        return self.name