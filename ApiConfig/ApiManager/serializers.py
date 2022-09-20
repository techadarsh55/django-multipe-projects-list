from rest_framework import serializers
from .models import EmployeeData,EmpForm

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeData
        fields = "__all__"