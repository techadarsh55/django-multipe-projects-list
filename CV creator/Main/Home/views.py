
from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import EmpForm
from .models import Emp


# Create your views here.
def index(request):
    return render(request,'home.html')

#def cvform(request):
    #return render(request,'cvform.html')


def insert1(request):
    e = Emp()
    e.name = 'adarsh'
    e.email = 'adarsh@gmail.com'
    e.contact = 7854269336
    e.skill = 'python, sql,django'
    e.experiance = 2
    e.hsc = 55
    e.ssc = 85
    e.gradue = 60
    e.hobby = 'travaling,cycling,cooking,paninting'
    e.save()
    return redirect("/")

def insert2(request):
    if request.method=="POST":
        e = Emp()
        e.name = request.POST.get('name')
        e.email = request.POST.get('email')
        e.contact = request.POST.get('contact')
        e.skill = request.POST.get('skill')
        e.experiance = request.POST.get('exp')
        e.hsc = request.POST.get('hsc')
        e.ssc = request.POST.get('ssc')
        e.gradue = request.POST.get('gradue')
        e.hobby = request.POST.get('hobby')
        e.save()
        return redirect("/")
    else:
        return render(request,'cvform.html')

def cvreviews(request):
    ul = Emp.objects.all()
    d = {"ul":ul}
    return render(request,'cvreview.html',d)

def user_list(request):
    ul1 = Emp.objects.all()
    d1 = {"ul1":ul1}
    return render(request,'userlist.html',d1)

def emp_delete(request):
    eid = request.GET.get("id")
    emp = Emp.objects.get(id=eid)
    emp.delete()    
    return redirect("/userlist")

def emp_edits(request,id):
    emp = Emp.objects.get(id=id)
    if request.method=="POST":
        f = EmpForm(request.POST,instance=emp)
        f.save()
        return redirect("/userlist")
    else:
        f = EmpForm(instance=emp)
        context = {"form":f}
        return render(request,'cvform2.html',context)

