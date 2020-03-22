from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home),
    path("sign",views.sign,name="signIn"),
    path("postsign",views.postsign),
    path("logout",views.logout,name="logo"),
    path("signup",views.signUp,name='signup'),
    path("postsignup",views.postsignup,name='postsignup'),
    path("xcel",views.xcel),
 
 
]
