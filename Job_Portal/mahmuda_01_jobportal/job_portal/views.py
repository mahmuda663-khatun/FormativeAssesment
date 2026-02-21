from django.shortcuts import render, redirect
from job_portal.models import*
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(r):
    return render (r,'home.html')

def signup(r):
    if r.method=='POST':
       username=r.POST.get('username') 
       display_name=r.POST.get('display_name') 
       user_type=r.POST.get('user_type') 
       email=r.POST.get('email') 
       password=r.POST.get('password') 
       confirm_password=r.POST.get('confirm_password')

       user_exit= AuthUserModel.objects.filter(username=username).exists()
       if user_exit:
           messages.warning(r,'user already exits')
           return redirect('signup')
       
       
       if confirm_password==password:
           AuthUserModel.objects.create_user(
               username=username,
               display_name=display_name,
               user_type=user_type,
               email=email,
               password=password
           )
        
           messages.success(r,'successfully register')
           return redirect ('signin')
    return render (r,'signup.html')

def signin(r):
    if r.method=='POST':
       username=r.POST.get('username') 
       password=r.POST.get('password') 
    
       user=authenticate(r,username=username,password=password)

       if user:
           login(r,user)
           messages.success(r,'successfully login')
           return redirect('home')
       else:
           messages.warning(r,'invalid')
           return redirect(signin)
    return render (r,'signin.html')

def signout(r):
    logout(r)
    return redirect('signin') 
