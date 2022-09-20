from django.contrib import admin
from django.urls import include, path
from home import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",v.index),
    path("create_resume",v.resume_form),
    path("rlist",v.resumelist),
    path("views/<int:id>",v.viewresume),
    path("edit/<int:id>",v.edit_detail),
    path('delete/<int:id>',v.delete_data),
    

    
]