from django.shortcuts import redirect, render, HttpResponse
from matplotlib.style import context
from psutil import users
from .forms import UserForm1,UserForm2,UserForm4,UserForm3,UserForm5,UserInfo
# Create your views here.
def add_user1(request):
    if request.method == "POST":
        f = UserForm1(request.POST)
        f.save()
        return redirect("/")
    else:
        context = {"form":UserForm1}
        return render(request,"form.html",context)


def add_user2(request):
    if request.method=="POST":
        f = UserForm2(request.POST)
        f.save()
        return redirect("/")
    else:
        context = {"form":UserForm2}
        return render(request,"form.html",context)

def add_user3(request):
    if request.method=="POST":
        f = UserForm3(request.POST)
        f.save()
        return redirect("/")
    else:
        context = {"form":UserForm3}
        return render(request,"form.html",context)


def add_user4(request):
    if request.method=="POST":
        f = UserForm4(request.POST)
        f.save()
        return redirect("/")
    else:
        context = {"form":UserForm4}
        return render(request,"form.html",context)


def add_user5(request):
    if request.method=="POST":
        f = UserForm5(request.POST)
        f.save()
        return redirect("/")
    else:
        context = {"form":UserForm5}
        return render(request,"form.html",context)

from django.contrib.auth import authenticate,login,logout
def login_view(request):
    if request.method=="POST":
        uname = request.POST.get("username")
        passw = request.POST.get("password")
        user = authenticate(request,username = uname,password=passw)
        if user is not None:
            print("=============>",user.id,user.first_name,user.email)
            print("===>",uname,passw)
            login(request,user)
            return redirect("/")
        else:
            return HttpResponse("<h1>Invalid Entry</h2>")
    else:
        return render(request,"login.html")


def logout_view(request):
    logout(request)
    return redirect("/")