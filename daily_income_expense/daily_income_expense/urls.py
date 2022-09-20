
from argparse import Namespace
from django.contrib import admin
from django.urls import path,include
from user.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home),
    path('user-',include(('user.urls','user'),namespace="u")),
    path('income-',include(('income.urls','income'),namespace='inc')),
    path('expense-',include(('expense.urls','expense'),namespace='exp')),


]
