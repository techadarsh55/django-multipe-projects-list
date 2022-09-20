from django.urls import path
from .import views as v
#from secondapp import views as sv

urlpatterns = [
    path('first',v.fir),
    path('second',v.sec),
    path('second_home',v.sec_index),
    path('registeruser',v.register),
    path('adduser1',v.adduser1),
    path('adduser2',v.adduser2),
    path('user_list',v.user_list),
    path('register2',v.register2)

  
]