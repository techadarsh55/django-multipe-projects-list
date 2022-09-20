from django.contrib import admin
from django.urls import path,include
from Home import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.index),
    path('',include('Home.urls')),
    
]
