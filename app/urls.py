from django.urls import path
from . import views
from .views import TestPage,ListViewPage

urlpatterns = [
    path('', views.home, name='home'),
    path('Login/',views.Login,name='Login'),
    path('SignUp/',views.SignUp,name='SignUp'),
    path('Log_out/',views.Log_out,name='Log_out'),
    path('userprofile/',views.UserProfile,name='UserProfile'),
    path('superuser/',views.superuser,name='superuser'),
    path('viewitem/<str:pk>',views.viewitem,name='viewitem'),
    path("testpage/<int:pk>",TestPage.as_view(),name="testpage"),
    path("listviewpage/",ListViewPage.as_view(),name="listviewpage"),
    path("index2/",views.index2,name="index2"),
    
]
