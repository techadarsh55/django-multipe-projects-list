from django.urls import path
from .import views as v

urlpatterns = [
    path('',v.home),
    path("user_register",v.registeruser),
    path("user_list",v.userlist),

]