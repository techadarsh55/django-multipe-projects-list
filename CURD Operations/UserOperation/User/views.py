from certifi import contents
from django.shortcuts import redirect, render
from matplotlib.style import context
from .forms import Emp,EmpForm

# Create your views here.
def index(request):
    return render(request,"home.html")

def register(request):
    if request.method=="POST":
        f = EmpForm(request.POST)
        f.save()
        print(f.fields.values())
        return redirect("/")
    else:
        context={"form":EmpForm}
        return render(request,"register.html",context)

def emplist(request):
    f = Emp.objects.all()
    context = {'data':f}
    return render(request,"Emplist.html",context)

def delete(request,id):
    f = Emp.objects.get(id=id)
    f.delete()  
    return redirect("/")

def update(request,id):
    emp = Emp.objects.get(id=id)
    if request.method=="POST":
        f = EmpForm(request.POST,instance=emp)
        f.save()
        return redirect("/")
    else:
        f = EmpForm(instance=emp)
        context = {'form':f}
        return render(request,'update.html',context)
