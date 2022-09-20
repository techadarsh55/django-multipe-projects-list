from django.urls import path
from mynotes import views as v
urlpatterns = [
    path('addnote',v.AddForm.as_view()),
    path('savedata',v.SaveNote.as_view()),
    path('editnote/<int:pk>',v.UpdateNotes.as_view()),
    path('deletenote/<int:pk>',v.DeleteNote.as_view()),
    #path('listnote',v.listof_note),
    
    
    
]
