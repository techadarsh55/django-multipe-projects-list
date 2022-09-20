from django.shortcuts import redirect, render

# Create your views here.
def second(request):
    return render(request,'sec_1.html')

def index_h(request):
    return render(request,'index.html')