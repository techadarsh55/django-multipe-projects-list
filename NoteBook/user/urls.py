from django.urls import path
from user import views as v
urlpatterns = [
   
   path('New-Reg',v.Reg,name='newaccount'),
   path('login-user',v.Login),
   path('logout',v.Logout),
   
   
   
    
]
