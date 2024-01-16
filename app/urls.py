from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Login/',views.Login,name='Login'),
    path('SignUp/',views.SignUp,name='SignUp'),
    path('Log_out/',views.Log_out,name='Log_out'),
    path('userprofile/',views.UserProfile,name='UserProfile')
]
