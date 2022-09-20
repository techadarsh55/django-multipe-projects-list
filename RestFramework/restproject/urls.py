from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from restproject import views as v

urlpatterns = [
    path("",v.Home.as_view()),
    path("addemp",v.AddEmp.as_view()),
    path("el",v.EmpList.as_view()),
    path("createlist",v.createlistemp.as_view()),
    path("demp/<int:pk>",v.Deleteemp.as_view()),
    path("uemp/<int:pk>",v.Updateemp.as_view()),
    path("gemp/<int:pk>",v.GetEmp.as_view()),
    path("guemp/<int:pk>",v.GUemp.as_view()),
    path("gdemp/<int:pk>",v.GDemp.as_view()),
    path("gudemp/<int:pk>",v.GUDemp.as_view()),
    path("user1",v.UserSerial.as_view()),
    path("userview",v.Userview.as_view()),
    path("userdel/<int:pk>",v.UserDelete.as_view()),










]