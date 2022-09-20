
from django.contrib import admin
from django.urls import path,include
from index import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.HomeView.as_view()),
    path('',include('index.urls')),
    path('',include('mynotes.urls')),
    path('',include('listofnotes.urls')),
    path('',include('user.urls')),
    
    
    
]
