from importlib import import_module
from django.urls import path
from gallery import views as v
from .views import ShowImg
urlpatterns = [
    path('gallery',v.gallery,name="gallery"),
    path('showimg',ShowImg.as_view()),

]