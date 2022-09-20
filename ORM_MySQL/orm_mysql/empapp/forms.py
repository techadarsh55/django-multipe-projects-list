from attr import fields
from django import forms
from .models import Emp,EmpQuali,EmpQuali2, EmpQuali3,Singers,Songs,Songs2

class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields="__all__"

class EmpQualiForm(forms.ModelForm):
    class Meta:
        model=EmpQuali
        fields="__all__"

class EmpQualiForm2(forms.ModelForm):
    class Meta:
        model=EmpQuali2
        fields="__all__"

class EmpQualiForm3(forms.ModelForm):
    class Meta:
        model=EmpQuali3
        fields="__all__"


class SingerForm(forms.ModelForm):
    class Meta:
        model = Singers
        fields ="__all__"

class SongForm(forms.ModelForm):
    class Meta:
        model = Songs
        fields = "__all__"
 
class SongForm2(forms.ModelForm):
    class Meta:
        model = Songs2
        fields ="__all__"