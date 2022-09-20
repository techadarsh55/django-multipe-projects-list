from django.shortcuts import render
from django.views.generic import TemplateView,FormView,CreateView,ListView
from .forms import EmpForm, EmpRegister,UserData,UserForm

from rest_framework import generics as g
from .serializers import User,UserData
# Create your views here.
class Homeview(TemplateView):
    template_name ="index.html"

class RegisterView(FormView):
    form_class = UserForm
    template_name = "register.html"

class AddEmpView(CreateView):
    model = UserData
    fields ="__all__"
    success_url = "/"

class EmpList(ListView):
    model = UserData
    template_name = "emplist.html"

'''api base '''

class Userview(g.CreateAPIView):
    queryset = UserData
    serializer_class = User

class createempapi(g.ListCreateAPIView):
    model = UserData.objects.all()
    serializer_class = User
class listview(g.ListCreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = User

class EmpList1(g.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = User
