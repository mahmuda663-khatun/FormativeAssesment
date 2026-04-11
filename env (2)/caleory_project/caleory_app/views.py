from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from caleory_app.models import *
from django.contrib import messages
from caleory_app.forms import *
from datetime import date
from django.db.models import Sum
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def register_function(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'User already exists.')
            return redirect('register_function')
        if password == confirm_password:
            User.objects.create_user(
                username= username, 
                email=email,
                password=password,
            )

            subject= "Account Info"
            recipient_email= email
            sender_email=settings.EMAIL_HOST_USER
            context = {
                'username':username,
                'email': email,
                'password': password
            }
            html_content= render_to_string("emails/confirm-mail.html", context)

            email_send= EmailMultiAlternatives(subject, "" , sender_email, [recipient_email])
            email_send.attach_alternative(html_content, "text/html")
            email_send.send()    

            messages.success(request, 'User register successfully')
            return redirect('login_function')
        else:
            messages.error(request, 'Both password not match.')
            return redirect('register_function')

    return render(request, 'auth/register.html')

def login_function(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'auth/login.html')

def dashboard(request):
    current_date = date.today()
    current_user = request.user

    consumed_calorie = CaleoryConsumedModel.objects.filter(user = current_user, date = current_date)
    
    total_consumed = CaleoryConsumedModel.objects.filter(user = current_user, date = current_date).aggregate(total = Sum('caleory_consumed'))['total'] or 0
    bmr = current_user.user_profile.bmr or 0
  
    
    less_more_consumed = float(bmr) - float(total_consumed)
    
    context = {
        'consumed_calorie':consumed_calorie,
        'bmr': bmr, 
        'total_consumed': total_consumed,
        'less_more_consumed': less_more_consumed
    }
    return render(request, 'dashboard.html',context)

def logout_function(request):
    logout(request)
    return redirect('login_function')

def profile_page(request):

    return render(request, 'profile.html')

def profile_update(request):
    try:
        user_data = ProfileModel.objects.get(user = request.user)
        
    except ProfileModel.DoesNotExist:
        user_data = None

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=user_data)
        if profile_form.is_valid():
            profile_data = profile_form.save(commit=False)
            profile_data.user = request.user
            if profile_data.gender == 'Male':
                profile_data.bmr = 66.47 + (13.75 * profile_data.weight) + (5.003 * profile_data.height) - (6.755 * profile_data.age)
            else:
                profile_data.bmr = 655.1+(9.563 * profile_data.weight)+(1.850 * profile_data.height) - (4.676 * profile_data.age)
            profile_data.save()
            return redirect('profile_page')
    else:
        profile_form = ProfileForm(instance=user_data)

    context = {
        'profile_form':profile_form
    }

    return render(request, 'profile-update.html', context)


#---Consumed Calorie
def consumed_calorie(request):
    calorie_data = CaleoryConsumedModel.objects.filter(user = request.user)

    context = {
        'calorie_data': calorie_data
    }
    return render(request, 'consumed-calorie.html',context)

def add_calorie(request):
    if request.method == 'POST':
        calorie_form = CalorieForm(request.POST)
        if calorie_form.is_valid():
            calorie_form_data = calorie_form.save(commit=False)
            calorie_form_data.user = request.user
            calorie_form_data.save()
            return redirect('consumed_calorie')
        
    calorie_form = CalorieForm()

    context = {
        'calorie_form': calorie_form,
        'title': 'Add Consumed Calorie Info',
        'button':'Add Calorie',
    }

    return render(request, 'calorie-form.html',context)


def edit_calorie(request, pk):
    calorie_data = CaleoryConsumedModel.objects.get(id = pk)
    if request.method == 'POST':
        calorie_form = CalorieForm(request.POST, instance=calorie_data)
        if calorie_form.is_valid():
            calorie_form_data = calorie_form.save(commit=False)
            calorie_form_data.user = request.user
            calorie_form_data.save()
            return redirect('consumed_calorie')
        
    calorie_form = CalorieForm(instance=calorie_data)

    context = {
        'calorie_form': calorie_form,
        'title': 'Update Consumed Calorie Info',
        'button':'Update Calorie',
    }

    return render(request, 'calorie-form.html',context)


def delete_calorie(request, pk):
    CaleoryConsumedModel.objects.get(id = pk).delete()
    return redirect('consumed_calorie')