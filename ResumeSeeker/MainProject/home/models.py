from django.db import models

# Create your models here.
class Resume(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    Contact = models.IntegerField()
    Address = models.TextField(max_length=500)
    Linkedin = models.CharField(max_length=200)
    Github = models.CharField(max_length=200)
    skill = models.TextField(max_length=300)
    ssc = models.IntegerField()
    hsc = models.IntegerField()
    graud = models.IntegerField()
    certification = models.TextField(max_length=500)
    Lang = models.TextField(max_length=100)

    class Meta:
        db_table ="ResumeCheck"