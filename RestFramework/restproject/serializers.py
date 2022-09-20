from rest_framework import serializers
from .models import Emp,User1
#from django.contrib.auth.models import User

class User(serializers.ModelSerializer):
    class Meta:
        model= Emp
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User1
        fields = "__all__"
