from django.urls import path
from login import views as lv
urlpatterns = [

    path('userreg',lv.userreg),
    path("adduser1",lv.add_user1),
    path("adduser2",lv.add_user2),
    path("login",lv.login_user),
    path("logout",lv.logout_user),
    


]