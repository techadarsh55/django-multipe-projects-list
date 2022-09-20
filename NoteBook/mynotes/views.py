from re import template
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,FormView,UpdateView,DeleteView
from .forms import AddNoteForms,AddNotes
from user import *
# Create your views here.


    
class AddForm(FormView):
    form_class = AddNoteForms
    template_name ='form.html'
    
    
class SaveNote(CreateView):
    model = AddNotes
    fields = "__all__"
    success_url = "/"
    
class UpdateNotes(UpdateView):
    model = AddNotes
    fields = "__all__"
    success_url = "/" 
    
class DeleteNote(DeleteView):
    model = AddNotes
    success_url ="/"
'''   
def listof_note(request):
    cid = request.session.get('id')
    incl = AddNotes.objects.filter(user=cid)
    context = {'form':incl}
    return render(request,'listnote.html',context)'''