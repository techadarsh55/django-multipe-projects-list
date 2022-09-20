from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request,"home.html")
    
def add_user(request):
    if request.method=='POST':
        f = UserCreationForm(request.POST)
        f.save
        return redirect("/")
    else:
        context = {'form':UserCreationForm,'fmsg':'UserFrom'}
        return render(request,"form.html",context)

def user_list(request):
    f = User.objects.all()
    context = {'form':f}
    return render(request,'list.html',context)