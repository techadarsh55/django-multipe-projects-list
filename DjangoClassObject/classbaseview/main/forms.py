from attr import fields
from django import forms
from .models import EmpRegister,UserData
class EmpForm(forms.ModelForm):
    class Meta:
        model = EmpRegister
        fields = "__all__"
    
class UserForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = "__all__"