from xml.parsers.expat import model
from attr import field
from django import forms
from .models import EmpName
from django.contrib.auth.models import User

class EmpForm(forms.ModelForm):
    class Meta:
        model = EmpName
        fields = "__all__"
    
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "first_name","last_name",'email','username','password'