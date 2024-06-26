from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .models import UserModel

# Create your views here.

def indexPage(request):
    return render(request,'index.html')



def registerPage(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pword=request.POST.get('password')
        
        if uname=="" or email=="" or pword=="":
            query="All fields are required!"
            return render(request,'index.html',{'query':query})
        
        elif UserModel.objects.filter().exists():
            msg="Hi " + uname + " welcome back! "
            return render(request,'index.html',{'msg':msg})
        else:
            UserModel.objects.create(username=uname,email=email,password=pword)
            msg="Hi " + uname + " your registration was successful!"
            return render(request,'register.html',{'msg':msg})
    return render(request,'register.html')



def logoutPage(request):
    return render(request,'logout.html')
