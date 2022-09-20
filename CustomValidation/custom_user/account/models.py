from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, username, company_name, phone, password=None):
        if not email:
            raise ValueError("Email is required")
        if not company_name:
            raise ValueError("company name is required")
        if not phone:
            raise ValueError("active phone is required")
        if not username:
            raise ValueError("username is required")

        user=self.model(
            username=username,
            email=email,
            company_name=company_name,
            phone=phone

        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, company_name, phone, password=None):
        user=self.create_user(
            email=email,
            username = username,
            company_name=company_name,
            phone=phone,
            password=password,
        )
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField(verbose_name="Email Address", max_length=60,unique=True)
    company_name = models.CharField(verbose_name="Company Name",max_length=50, unique=True)
    phone = models.CharField(max_length=20)
    date_joined = models.DateTimeField(verbose_name="Date joined",auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Late login",auto_now=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = ["company_name","phone","email"]

    objects = MyUserManager()

    def __str__(self):
        return self.company_name

    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perm(self, app_label):
        return self.is_superuser

