from django.urls import path
from listofnotes import views as v
urlpatterns = [
    
    path('listofnote',v.listview),
    
]
