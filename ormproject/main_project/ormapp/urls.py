from django.contrib import admin
from django.urls import path,include
from ormapp import views as v


urlpatterns = [
    path('',v.home),
    path('insert1',v.insert ),
    path('insert2',v.insert2),
    path('insert3',v.insert3),
    path('insert4',v.insert4),
    path('userlist',v.usetlist),
    path('delete_emp',v.emp_delete),
    path('delete_emp2/<int:id>',v.emp_delete2),
    path('editemp/<int:id>',v.edit_emp)


]