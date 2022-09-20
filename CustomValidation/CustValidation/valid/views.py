from django.shortcuts import redirect, render
from .forms import EmpName,EmpForm,User,UserForm
from django.views.generic import TemplateView,FormView,CreateView
# Create your views here.
def index(request):
    return render(request,'index.html')

def add(request):
    if request.method=='POST':
        f = EmpForm(request.POST)
        f.save()
        return redirect("/")
    else:
        f = EmpName.objects.all()
        context = {'form':EmpForm}
        return render(request,'form.html',context)

class UserF(FormView):
    form_class = UserForm
    template_name ="form1.html"

class Adduser(CreateView):
    queryset = User.objects.all()
    fields = ["first_name","last_name","email","username","password"]
    success_url ="/"