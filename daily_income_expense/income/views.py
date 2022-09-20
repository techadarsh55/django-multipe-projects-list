from django.shortcuts import render,redirect

from .models import Income,IncomeForm


def add_income(request):
    if request.method=='POST':
        f=IncomeForm(request.POST)
        f.save()
        return redirect('/')
    else:
        context={'form':IncomeForm,'fmsg':"IncomeForm"}
        return render(request,'form.html',context)

def income_list(request):
    context={"incl":Income.objects.all()}
    return render(request,'inclist.html',context)