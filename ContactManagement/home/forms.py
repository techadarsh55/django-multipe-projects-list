from dataclasses import field
from django import forms
from .models import Register
#registyer form
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = "__all__"
