
from django.shortcuts import redirect, render
from django.views.generic import ListView
from mynotes.models import AddNotes
from mynotes.models import *
from django.contrib.auth.models import User

import user
# Create your views here.


def listview(request):
    #uid = request.session.get('id')
    if request.session.has_key('username'):
        #uid = request.session['username'] = request.session.get('user')
        #s = User.objects.filter(uname = request.user)
        f = AddNotes.objects.filter()
        context = {'list':f}
        return render(request,'yourNotes.html',context)
    else:
        return redirect('/login-user')
