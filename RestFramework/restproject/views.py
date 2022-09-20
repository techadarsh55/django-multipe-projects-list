from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics as g
from restproject.models import User1
from .serializers import User,Emp,UserSerializer

# Create your views here.

class Home(TemplateView):
    template_name ="home.html"

class AddEmp(g.CreateAPIView):
    queryset = Emp
    serializer_class = User

class EmpList(g.ListAPIView):
    queryset = Emp.objects.all()
    serializer_class = User

class createlistemp(g.ListCreateAPIView):
    queryset  = Emp.objects.all()
    serializer_class = User

class Deleteemp(g.DestroyAPIView):
    queryset = Emp.objects.all()
    serializer_class = User

class Updateemp(g.UpdateAPIView):
    queryset = Emp.objects.all()
    serializer_class = User

class GetEmp(g.RetrieveAPIView):
    queryset = Emp.objects.all()
    serializer_class =User

class GUemp(g.RetrieveUpdateAPIView):
    queryset = Emp.objects.all()
    serializer_class = User

class GDemp(g.RetrieveDestroyAPIView):
    queryset = Emp.objects.all()
    serializer_class = User

class GUDemp(g.RetrieveUpdateDestroyAPIView):
    queryset = Emp.objects.all()
    serializer_class = User

#User from django admin

class UserSerial(g.CreateAPIView):
    queryset = User1
    serializer_class = UserSerializer

class Userview(g.ListAPIView):
    queryset = User1.objects.all()
    serializer_class = UserSerializer

class UserDelete(g.DestroyAPIView):
    queryset = User1.objects.all()
    serializer_class = UserSerializer