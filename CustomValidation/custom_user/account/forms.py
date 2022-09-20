from attr import field
from django import forms
from .models import MyUser,MyUserManager

class UserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields ="__all__"
