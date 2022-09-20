from django.urls import path
from ApiManager import views as v
from django.views.generic import TemplateView

urlpatterns = [
    path("",v.home.as_view()),
    path("employee-form",v.Register),
    path("addemployee",v.AddEmp.as_view()),


]
