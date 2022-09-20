from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(User):
    age = models.IntegerField()
    gender = models.CharField(max_length=7)
    contact = models.CharField(max_length=10)
    class Meta:
        db_table ="userinfo"