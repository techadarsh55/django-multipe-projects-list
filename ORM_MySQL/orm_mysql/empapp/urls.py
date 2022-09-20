
from django.contrib import admin
from django.urls import path
from .import views as v
urlpatterns = [
    path("",v.home),
    path("empr",v.addemp),
    path("empq",v.add_qualif),
    path("eqlist",v.emp_qualif_list),
    path("empq2",v.add_qualif2),
    path("eqlist2",v.emp_qualif_list2),
    path("empq3",v.add_qualif3),
    path("eqlist3",v.emp_qualif_list3),
    path("singer",v.add_singers),
    path("songs",v.add_songs),
    path("singer_list",v.singers_list),
    path("FSongs",v.Singer_form)


    
]
