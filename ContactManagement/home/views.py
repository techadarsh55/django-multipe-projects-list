from winreg import REG_QWORD
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from .forms import Register,RegisterForm
#home section
def Home(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')


def RegissterView(request):
    if request.method == "POST":
        data = RegisterForm(request.POST)
        
        if data.is_valid():

            data.save()
            #print(data)
            return redirect("/")
        else:
            return HttpResponse('<h2>invalid data</h2>')
    else:
        context = {'user':RegisterForm}
        return render(request,'register.html',context)


def Login(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        passwd = request.POST.get("password")
        home_register = authenticate(request,username = uname,password=passwd)
        if home_register is not None:
            print(uname,passwd)
            login(request,home_register)
            return redirect("/")
        else:
            return HttpResponse("<h2>wrong</h2>")
    else:
        return render(request,'index.html')