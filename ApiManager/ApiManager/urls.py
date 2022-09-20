
from django.contrib import admin
from django.urls import path,include
from ApiIntergration import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.Home.as_view()),
    path('',include('ApiIntergration.urls')),

]
