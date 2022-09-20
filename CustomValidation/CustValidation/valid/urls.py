from django.urls import path
from valid import views as v
from django.views.generic import TemplateView

urlpatterns = [
    path("",v.index),
    path("add",v.add),
    path("add1",v.UserF.as_view()),
    path("saveemp",v.Adduser.as_view()),
    



]