
from django.urls import path
from user import views as v
from income import views as ic
urlpatterns = [

    path("adduser",v.add_user,name="add"),
    path('income',ic.add_income,name="income")

]
