from django.urls import path
from django.views.generic import TemplateView
from index import views as v

urlpatterns = [
    path('',v.HomeView.as_view()),
    
    
    
]
