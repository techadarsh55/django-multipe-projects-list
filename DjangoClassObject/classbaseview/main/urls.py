from django.urls import path
from main import views as v

urlpatterns =[
    path("",v.Homeview.as_view()),
    path("register",v.RegisterView.as_view()),
    path("saveemp",v.AddEmpView.as_view()),
    path("emplist",v.EmpList.as_view()),
    path("register",v.Userview.as_view()),
    path("listv",v.createempapi.as_view()),
    path("el",v.EmpList1.as_view()),
    path("cl",v.listview.as_view()),
    






]