from django.urls import path
from .import views as sv

urlpatterns = [
  path('second',sv.second),
  path('sec_index',sv.index_h)

]