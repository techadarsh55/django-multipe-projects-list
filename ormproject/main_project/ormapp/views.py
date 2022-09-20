import email
from multiprocessing import context
from django.shortcuts import redirect, render
from ormapp.models import Emp
from ormapp.forms import EmpForm,EmpForm1
# Create your views here.
def home(request):
    return render (request,'home.html')
    
def insert(request):
    e = Emp()
    e.name = "adarsh"
    e.email = "adarsh@hotmail.com"
    e.contact = 78451963
    e.save()
    return redirect("/")

def insert2(request):
    if request.method=='POST':
        e =Emp()
        e.name= request.POST.get('name')
        e.email= request.POST.get('email')
        e.contact= request.POST.get('contact')
        e.save()
        return redirect("/")
    else:
        return render(request,"register.html")


def insert3(request):
    if request.method=='POST':
        f = EmpForm(request.POST)
        f.save()
        return redirect("/")
    else:
        d = {"form":EmpForm}
        return render(request,'register2.html',d)

def insert4(request):
    if request.method=='POST':
        f = EmpForm1(request.POST)
        f.save()
        return redirect("/")
    else:
        d = {"form":EmpForm1}
        return render(request,'register4.html',d)

def usetlist(request):
    ul = Emp.objects.all()
    d = {"ul":ul}
    return render(request,'register5.html',d)

def emp_delete(request):
    eid=request.GET.get("id")
    emp = Emp.objects.get(id=eid)
    emp.delete()
    return redirect("/userlist")

def emp_delete2(request,id):
    emp =Emp.objects.get(id=id)
    emp.delete()
    return redirect("/userlist")

def edit_emp(request,id):
    emp = Emp.objects.get(id=id)
    if request.method=="POST":
        f=EmpForm(request.POST,instance=emp)
        f.save()
        return redirect("/userlist")
    else:
        f =EmpForm(instance=emp)
        context = {"form":f}
        return render(request,"register2.html",context)
