from rest_framework import serializers
from .models import ProductInfo
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInfo
        fields = "__all__"
        