from django.contrib import admin
from django.urls import path
from User import views as v
urlpatterns = [
    path("",v.index),
    path("reg",v.register),
    path("elist",v.emplist),
    path("delete/<int:id>",v.delete),
    path("edit/<int:id>",v.update),
    





]
