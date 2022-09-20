from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'
    
class MainPage(TemplateView):
    template_name = 'home.html'
