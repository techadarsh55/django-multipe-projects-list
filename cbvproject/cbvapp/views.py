from django.views.generic import TemplateView,FormView,CreateView,ListView,DeleteView,UpdateView
from django.views.generic.edit import CreateView
from .models import Emp,EmpFrom
# Create your views here.

class Demo(TemplateView):
    template_name = "demo.html"

class EmpRegistration(FormView):
    form_class = EmpFrom
    template_name ="form.html"

class CreateEmp(CreateView):
    model= Emp
    fields="__all__"
    success_url ="/"

class EmpListView(ListView):
    model= Emp
    template_name="emplist.html"

class DeleteEmp1(DeleteView):
    model = Emp
    success_url="/"

class DeleteEmp2(DeleteView):
    model = Emp
    template_name="delete.html"
    success_url="/"

class UpdateEmp(UpdateView):
    model = Emp
    fields ="__all__"
    success_url="/"
    
        
    


