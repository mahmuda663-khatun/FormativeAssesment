from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import*
from .models import*
from django.db.models import Sum

def register_view(r):
    if r.method == 'POST':
        form = RegisterForm(r.POST)
        if form.is_valid():
            user = form.save()
            login(r,user)
            return redirect('login')
        
    form = RegisterForm()
    context={
        'form':form
    }
    return render (r,"register.html",context)

def Login_view(r):
    if r.method == 'POST':
        form = LoginForm(r, r.POST)
        if form.is_valid():
            user = form.get_user()
            login(r,user)
            return redirect('dashboard')
        
    form = LoginForm()
    context={
        'form':form
    }
    return render (r,"login.html",context)

def logout_view(r):
    logout(r)
    return redirect('login')

@login_required
def profile_view(request):
    try:
        profile = request.user.profile
    except PorfileModel.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = request.user
            w = prof.weight
            h = prof.height
            a = prof.age
            if prof.gender == 'Male':
                prof.bmr = 66.47 + (13.75 * w) + (5.003 * h) - (6.755 * a)
            else:
                prof.bmr = 655.1 + (9.563 * w) + (1.850 * h) - (4.676 * a)
            prof.User = request.user
            prof.save()
            return redirect('dashboard')

    form = ProfileForm(instance=profile)
    context={
        'form':form
    }
    return render(request, 'profile.html',context)

@login_required
def add_food_view(r):
    if r.method == 'POST':
        form = FoodEntryForm(r.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = r.user
            entry.save()
            return redirect('dashboard')
    
    form = FoodEntryForm()

    context={
        'form':form
    }
    return render(r, 'add_food.html', context)


@login_required
def dashboard_view(request):
    profile=PorfileModel.objects.filter(User=request.user).first()
    if profile:
        req_kcal = profile.bmr
    else:
        req_kcal = 0
    
    today = timezone.now().date()
    total_consumed = FoodEntryModel.objects.filter(user=request.user, date=today).aggregate(calories__sum=Sum('caloris'))['calories__sum'] or 0

    context = {
        'profile': profile,
        'total_consumed': total_consumed,
        'req_kcal':req_kcal
    }
    return render(request, 'dashboard.html', context)
