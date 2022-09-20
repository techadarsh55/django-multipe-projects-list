import imp
from django.shortcuts import render
from .forms import MyUser,UserForm
from django.views.generic import TemplateView,FormView,CreateView
# Create your views here.
def index(request):
    return render(request,"index.html")
    
class UserView(FormView):
    form_class = UserForm
    template_name ="form.html"

class AddDate(CreateView):
    queryset = MyUser.objects.all()
    fields ="__all__"
    success_url ="/"