from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Userinfo
from .forms import UserForm1,UserFrom2,UserForm3
# Create your views here.
def user_login(request):
    return render(request,'login.html')

def userreg(request):
    if request.method=="POST":
        f = UserForm1(request.POST)
        f.save()
        return redirect("/")
    else:
        context = {"forms":UserForm1}
        return render(request,'register.html',context)


def add_user1(request):
    if request.method == "POST":
        f = UserFrom2(request.POST)
        f.save()
        return redirect("/")
    else:
        context = {"forms":UserFrom2}
        return render(request,'register.html',context)


def add_user2(request):
    if request.method == "POST":
        f = UserForm3(request.POST)
        f.save()
        return redirect("/")
    else:
        context = {"forms":UserForm3}
        return render(request,'register.html',context)


from django.contrib.auth import authenticate,login,logout

def login_user(request):
    if request.method=="POST":
        uname = request.POST.get("username")
        passw = request.POST.get("password")
        user = authenticate(request,username = uname,password =passw)
        if user is not None:
            print("====>",user.id,user.email,user.first_name)
            print("===",uname,passw)
            print("Login Successfully")
            login(request,user)
            return redirect("/")

        else:
            return HttpResponse("<h2>Incoorect Username and password</h2>")
    else:
        return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect("/")
