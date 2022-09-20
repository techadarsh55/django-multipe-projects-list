from .models import UserDetail
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EmpForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = "__all__"


class UserFrom(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class UserForm2(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','is_active','date_joined','username','password1','password2']
        
