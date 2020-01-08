from django.urls import path
from . import views

urlpatterns = [
    path('home',views.homepage),
    path('signup',views.prosignup),
    path('login',views.loginn),
    path('custsignup',views.cussignup),
    path('prorgstn',views.profsignup),
    path('custregstn',views.custsignup),
    path('',views.homepage),
    path('search',views.search),
]