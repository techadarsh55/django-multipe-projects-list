from django.shortcuts import redirect, render

from index.models import employee
from .forms import registerForm
# Create your views here.

def home(request):
    return render(request,'home.html')

def registeruser(request):
    if request.method=="POST":
        f = registerForm(request.POST)
        f.save()
        return redirect("/")
    else:
        context = {"form":registerForm}
        return render(request,"form.html",context)

def userlist(request):
    qlist = employee.objects.all()
    return render(request,"userlist.html",{'ulist':qlist})

