from django.urls import path 
from . import views



urlpatterns = [
    path('',views.indexPage,name='index'),
    path('register/',views.registerPage,name='register'),
    path('logout/',views.logoutPage,name='logout'),
    
]
