from django.urls import path
from cbvapp import views as v
from django.views.generic import TemplateView

urlpatterns = [
    path("",TemplateView.as_view(template_name="home.html")),
    path("demo",v.Demo.as_view()),
    path("reg",v.EmpRegistration.as_view()),
    path("saveemp",v.CreateEmp.as_view()),
    path("emplistview",v.EmpListView.as_view()),
    path("d1/<int:pk>",v.DeleteEmp1.as_view()),
    path("d2/<int:pk>",v.DeleteEmp2.as_view()),
    path("e1/<int:pk>",v.UpdateEmp.as_view()),
    


   ]

