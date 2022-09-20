from dataclasses import fields
from django import forms
from .models import User,UserRegister

class NewUserForm(forms.ModelForm):
    class Meta:
        model = UserRegister
        fields = ['first_name','last_name','Age','Contact','email','Country','username','password']
        
from django.contrib.auth.forms import UserCreationForm

class UserReg(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]
        
        
class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","password1"]