from django.db import models
from django.core.exceptions import ValidationError



class Register(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(error_messages="please enter the gmail",max_length=60,validators=[ValidationError])
    Phone = models.IntegerField()
    Username = models.CharField(max_length=15)
    Password = models.CharField(help_text="Alpha & Numeric password",max_length=10)

    
    def __str__(self):
        return self.Username

    
    def emailcheck(Email, *args, **kwargs):
        if 'gmail.com' in Register.Email:
            pass
        else:
            raise ValidationError('Mail is not gmail',params={'Email':Email})


        


        

