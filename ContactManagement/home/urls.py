from django.urls import path
from home import views
urlpatterns = [
    path('',views.Home),
    path('reg',views.RegissterView),
    path('login',views.Login),
    path('home',views.index),

    
]
