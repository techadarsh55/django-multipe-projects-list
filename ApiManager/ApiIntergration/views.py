from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics as g
from .serializers import ProductInfo,ProductSerializer
# Create your views here.

class Home(TemplateView):
    template_name ='home.html'

class AddEmployee(g.CreateAPIView):
    queryset = ProductInfo
    serializer_class = ProductSerializer

class ListEmployee(g.ListAPIView):
    queryset = ProductInfo.objects.all()
    serializer_class = ProductSerializer

class Listemp(g.ListCreateAPIView):
    queryset = ProductInfo.objects.all()
    serializer_class = ProductSerializer