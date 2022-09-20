from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .forms import EmployeeData,EmpForm
from rest_framework import generics as g

# Create your views here.

class  home(TemplateView):
    template_name = "home.html"

def Register(request):
    if request.method=="POST":
        f = EmpForm(request.POST)
        f.save()
        return redirect("/")
    else:
        context = {'form':EmpForm}
        return render(request,'form.html',context)

from .serializers import EmpSerializer,EmployeeData,EmpForm

class AddEmp(g.CreateAPIView):
    queryset = EmployeeData
    serializer_class = EmpSerializer