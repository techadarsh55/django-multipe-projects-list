from django.urls import path
from ormsql import views as v
urlpatterns = [
    path("",v.index),
    path("login",v.login_view),
    path("auth1",v.auth_user),
    path("reg",v.register),
    path("auth2",v.auth_user2),
    path("logout",v.logout),
    



    

    
]