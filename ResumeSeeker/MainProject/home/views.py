from django.shortcuts import redirect, render
from .forms import ResumeForm,Resume
# Create your views here.

def index(request):
    return render(request,"home.html")

def resume_form(request):
    if request.method=="POST":
        f= ResumeForm(request.POST)
        f.save()
        return redirect("/")
    else:
        context={'form':ResumeForm}
        return render(request,"resumeform.html",context)

def resumelist(request):
    eq = Resume.objects.all()
    return render(request,"resumeentry.html",{'list1':eq})
'''
def viewreusme(request,id):
    res = Resume.objects.get(id=id)
    if request.method=="POST":
        f = ResumeForm(request.POST,instance=res)
        f.save()
        return("/rlist")
    else:
        f = ResumeForm(instance=res)
        context={'form':f}
        return render(request,'viewresume.html',context)

        '''
def viewresume(request,id):
    rs = Resume.objects.get(id=id)
    print("myoutput",rs)
    return render(request,"viewerdata.html",{'resumes':rs})

def edit_detail(request,id):
    rs = Resume.objects.get(id=id)
    if request.method=="POST":
        f = ResumeForm(request.POST,instance=rs)
        f.save()
        return redirect("/rlist")
    else:
        f = ResumeForm(instance=rs)
        context ={'form':f}
        return render(request,"resumeform.html",context)


def delete_data(request,id):
    rs = Resume.objects.get(id=id)
    rs.delete()
    return redirect("/rlist")