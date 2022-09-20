from django.shortcuts import redirect, render
datalist = []
# Create your views here.
def home(request):
    return render(request,"master.html")
def fir(request):
    return render(request,'first.html')
def sec(request):
    return render(request,'second.html')
def thr(request):
    return render(request,'third.html')
def sec_index(request):
    return render(request,'sec_1.html')
def register(request):
    return render(request,'register.html')

def adduser1(request):
    id=request.GET.get("id")
    n = request.GET.get("name")
    e = request.GET.get("eamil")
    c = request.GET.get("Contact")
    print(id,n,e,c)
    return redirect("/")

def adduser2(request):
    id=request.POST.get("id")
    n = request.POST.get("name")
    e = request.POST.get("email")
    c = request.POST.get("contact")
    print(id,n,e,c)
    return redirect("/")

def register2(request):
    if request.method=='POST':
        id=request.POST.get("id")
        name = request.POST.get("name")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        t = (id,name,email,contact)
        datalist.append(t)
        print(datalist)
        return redirect("/")
    else:
        return render(request,'adduser2.html')

def user_list(request):
    d = {"ul":datalist}
    return render(request,'user_list.html',d)