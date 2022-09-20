from django.urls import path
from .views import UserView,AddDate
from account import views as v

urlpatterns = [
    path("",v.index),
    path("form",UserView.as_view()),
    path("saveemp",AddDate.as_view()),
    


]
