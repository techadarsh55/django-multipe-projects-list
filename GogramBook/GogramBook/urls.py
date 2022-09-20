
from django.contrib import admin
from django.urls import path,include
from home import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home),
    path('',include('home.urls')),
    path('',include('post.urls')),
    path('',include('account.urls')),
    path('',include('search.urls')),
    
    
]
