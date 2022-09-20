
from django.urls import path
from ApiIntergration import views as v
from django.views.generic import TemplateView

urlpatterns = [
    path('Employee-insert',v.AddEmployee.as_view()),
    path('data-list',v.ListEmployee.as_view()),
    path('emplist',v.Listemp.as_view())

]
