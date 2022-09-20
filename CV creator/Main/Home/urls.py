from django.urls import path
from Home import views as v

urlpatterns = [
    path('',v.index),
    path('cvforms',v.insert1),
    path('cvforms2',v.insert2),
    path('cvreviews',v.cvreviews),
    path('userlist',v.user_list),
    path('delete_emp',v.emp_delete),
    path('edit_emp/<int:id>',v.emp_edits),



]
