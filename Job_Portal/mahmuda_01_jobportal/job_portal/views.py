from django.shortcuts import render, redirect
from job_portal.models import*
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash

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
           user=AuthUserModel.objects.create_user(
               username=username,
               display_name=display_name,
               user_type=user_type,
               email=email,
               password=password
           )
           if user:
               if user_type=='Recruiters':
                   Recruiters_profileModel.objects.create(
                       Recruiters = user
                   )
               else:
                   Seeker_profileModel.objects.create(
                       Jobseekers = user
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

def ChangePass(r):
    curent_user=r.user
    
    if r.method=='POST':
       current_password=r.POST.get('current_password') 
       new_password=r.POST.get('new_password') 
       confirm_password=r.POST.get('confirm_password')

       if check_password(current_password,curent_user.password):

           if new_password==confirm_password:
                curent_user.set_password(new_password)
                curent_user.save()
                update_session_auth_hash(r,curent_user)
                return redirect ('home')
    return render (r,'ChengePass.html')

def Recruiters_profilelist(r):
    r_data=Recruiters_profileModel.objects.all()
    context={
        'r_data':r_data
    }
    return render (r,'Recruiters_profilelist.html',context)