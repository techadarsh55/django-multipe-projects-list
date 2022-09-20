from attr import fields
from django import forms
from login.models import Userinfo,User

class UserForm1(forms.ModelForm):
    class Meta:
        model = Userinfo
        fields = ['username','first_name','last_name','Age','Gender','Contact','email','date_joined','password']


class UserFrom2(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

from django.contrib.auth.forms import UserCreationForm

class UserForm3(UserCreationForm):
    class Meta:
        model = Userinfo
        fields = ['first_name','last_name','Age','Gender','email','Contact','username','password1','password2']
