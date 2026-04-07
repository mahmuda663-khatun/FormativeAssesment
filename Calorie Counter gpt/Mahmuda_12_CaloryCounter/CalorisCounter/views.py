from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProfileForm, FoodEntryForm
from .models import Profile, FoodEntry
from django.utils import timezone
from django.db.models import Sum

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile') # redirect to create profile initially
    else:
        form = RegisterForm()
    return render(request, 'CalorisCounter/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=password)
            # if user is not None:
                user=form.get_user()
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'CalorisCounter/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = request.user
            # Calculate BMR
            # Male: BMR = 66.47 + (13.75 × weight) + (5.003 × height) − (6.755 × age)
            # Female: BMR = 655.1 + (9.563 × weight) + (1.850 × height) − (4.676 × age)
            w = prof.weight
            h = prof.height
            a = prof.age
            if prof.gender == 'Male':
                prof.bmr = 66.47 + (13.75 * w) + (5.003 * h) - (6.755 * a)
            else:
                prof.bmr = 655.1 + (9.563 * w) + (1.850 * h) - (4.676 * a)
            prof.save()
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'CalorisCounter/profile.html', {'form': form})

@login_required
def add_food_view(request):
    if request.method == 'POST':
        form = FoodEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('dashboard')
    else:
        form = FoodEntryForm()
    return render(request, 'CalorisCounter/add_food.html', {'form': form})

@login_required
def dashboard_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        return redirect('profile')
    
    today = timezone.now().date()
    entries = FoodEntry.objects.filter(user=request.user, date=today)
    total_consumed = entries.aggregate(Sum('calories'))['calories__sum'] or 0

    context = {
        'profile': profile,
        'entries': entries,
        'total_consumed': total_consumed,
        'required': profile.bmr if profile.bmr else 0,
    }
    return render(request, 'CalorisCounter/dashboard.html', context)
