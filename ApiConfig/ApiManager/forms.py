from django import forms
from .models import EmployeeData


class EmpForm(forms.ModelForm):
    class Meta:
        model = EmployeeData
        fields = "__all__"