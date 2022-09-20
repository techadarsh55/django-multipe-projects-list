
from django.db import models
from user.models import User
# Create your models here.
class AddNotes(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=500)
    date_create = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

          
    def __str__(self):
        return self.title
    