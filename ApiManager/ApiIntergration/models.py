from django.db import models

# Create your models here.
class ProductInfo(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    JobTitle = models.CharField(max_length=50)
    Email = models.EmailField(max_length=256)
    Phone = models.IntegerField()
    JoinDate = models.DateField()
    ProfileImage = models.CharField(max_length=2000)

    class Meta:
        db_table = "ProductData"