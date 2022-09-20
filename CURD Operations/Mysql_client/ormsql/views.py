from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import User,UserDetail,UserFrom,EmpForm,UserForm2
# Create your views here.
def index(request):
    return render(request,"index.html")

def auth_user(request):
    if request.method=="POST":
        f = UserFrom(request.POST)
        f.save()
        return redirect("/")
    else:
        context = {"form":UserFrom}
        return render(request,'auth1.html',context)
    
def auth_user2(request):
    if request.method=="POST":
        f = UserForm2(request.POST)
        f.save()
        return redirect("/")
    else:
        context = {"form":UserForm2}
        return render(request,'auth2.html',context)

def register(request):
    if request.method=="POST":
        f = EmpForm(request.POST)
        f.save()
        return redirect("/")
    else:
        context = {"form":EmpForm}
        return render(request,'register.html',context)

from django.contrib.auth import authenticate,login,logout
def login_view(request):
    if request.method =="POST":
        uname = request.POST.get('username')
        passwd = request.POST.get('password')
        user = authenticate(request,username=uname,password=passwd)
        if user is not None:
            print("===>",user.id,user.first_name,user.username,user.password)
            login(request,user)
            return redirect("/auth2")
        else:
            return HttpResponse("<h2>incorrect password and username</h2>")
    else:
        return render(request,"login.html")

def logout(request):
    logout(request)
    return redirect("/login")
