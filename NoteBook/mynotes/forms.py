from dataclasses import fields
from django import forms
from .models import AddNotes
class AddNoteForms(forms.ModelForm):
    class Meta:
        model = AddNotes
        fields = "__all__"
        