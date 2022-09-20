from django.shortcuts import HttpResponse

def first_call(request):
    return HttpResponse("<h1>Hii</h1>")
def second_call(request):
    return HttpResponse("<h2>Django Developer</h2>")

def home(request):
    return HttpResponse("<h1>home</h1>")