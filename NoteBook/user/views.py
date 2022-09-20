
from django.shortcuts import redirect, render,HttpResponse
from user.forms import NewUserForm,UserReg,LoginForm
# Create your views here.
#register_link
def Reg(request):
    if request.method=="POST":
        f = UserReg(request.POST)
        f.save()
        return redirect("/")
    else:
        context = {'form':UserReg}
        return render(request,'register.html',context)
    
 
from django.contrib.auth import authenticate,login,logout    
def Login(request):
    username = 'not logged in'
    if request.method=="POST":
        #username = LoginForm.cleaned_data['username']
        request.session['username']=username
        uname = request.POST.get("username")
        passw = request.POST.get("password")
        user = authenticate(request,username=uname,password=passw)
        if user is not None:
            print("====>Login Successfully",user.id,user.first_name)
            print(uname,passw)
            login(request,user)
            return redirect("/")
        else:
            return HttpResponse("<h2>Invalid Username & Password</h2>")
    else:
        context = {'form':LoginForm}
        return render(request,'login.html',context)
    

def Logout(request):
    #del request.session['username']
    logout(request)
    return redirect("/")    
