import imp
from attr import field
from rest_framework import serializers
from .models import UserData

class User(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = "__all__"