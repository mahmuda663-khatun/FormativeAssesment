from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from portfolio_app.models import *
from portfolio_app.forms import *
from django.contrib import messages

def register_page(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login_page') 
         
    user_form = RegisterForm()
    context ={
        'user_form':user_form,
    }       
    return render(request, 'register.html',context)

def login_page(request):
    if request.method == 'POST':
        user_form = LoginForm(request, request.POST)
        if user_form.is_valid():
            user = user_form.get_user()
            login(request, user)
            return redirect('dashboard')    
    user_form = LoginForm()
    context ={
        'user_form':user_form,
    }            
    return render(request, 'login.html',context)

def logout_Page(request):
    logout(request)
    return redirect('login_page')

def dashboard(request):
    
    return render(request, 'dashboard.html')

def profile_page(request):
    profile_data = ProfileModel.objects.first()
    context = {
        'profile_data': profile_data
    }
    return render(request, 'profile.html',context)

def update_profile(request):
    user = ProfileModel.objects.first()
    if request.method == 'POST':
        form_data = UpdateProfileForm(request.POST, request.FILES,instance=user)
        if form_data.is_valid():
            form_data.save()
            return redirect('profile_page')
    
    form_data = UpdateProfileForm(instance=user)
    
    context = {
        'form_data': form_data,
        'title': "Update Profile Info",
        'btn_name': 'Update Profile',
    }
    return render(request,'master/base-form.html',context)

def resume_page(request):
    profile_data = ProfileModel.objects.first()
    project_data = ProjectModel.objects.all()
    skill_data = SkillModel.objects.all()
    
    experience_data = ExperienceModel.objects.all()
    
    context = {
        "profile_data":profile_data,
        "skills": skill_data,
        "projects": project_data,
        'experiences': experience_data
    }
    
    
    return render(request, 'resume.html',context)

def project_list(request):
    project_data = ProjectModel.objects.all()
    
    context = {
        'project_data':project_data
    }
    
    return render(request, 'project-list.html',context )

def add_project(request):
    if request.method == 'POST':
        form_data = ProjectForm(request.POST, request.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect('project_list')
    
    form_data = ProjectForm()
    context = {
        'form_data': form_data,
        'title': "Add Project Info",
        'btn_name': 'Add Project',
    }
    return render(request, 'master/base-form.html',context)

def edit_project(request, id):
    data = ProjectModel.objects.get(id = id)
    if request.method == 'POST':
        form_data = ProjectForm(request.POST, request.FILES, instance=data)
        if form_data.is_valid():
            form_data.save()
            return redirect('project_list')
    
    form_data = ProjectForm(instance=data)
    context = {
        'form_data': form_data,
        'title': "Update Project Info",
        'btn_name': 'Update Project',
    }
    return render(request, 'master/base-form.html',context)

def delete_project(request, id):
    ProjectModel.objects.get(id = id).delete()
    return redirect('project_list')

def skill_list(request):
    skill_data = SkillModel.objects.all()
    
    context = {
        'skill_data': skill_data
    }
    
    return render(request, 'skill-list.html', context)

def add_skill(request):
    if request.method == 'POST':
        form_data = SkillForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('skill_list')
    
    form_data = SkillForm()
    context = {
        'form_data': form_data,
        'title': "Add Skill Info",
        'btn_name': 'Add Skill',
    }
    return render(request, 'master/base-form.html',context)

def edit_skill(request, id):
    data = SkillModel.objects.get(id = id)
    if request.method == 'POST':
        form_data = SkillForm(request.POST, instance=data)
        if form_data.is_valid():
            form_data.save()
            return redirect('skill_list')
    
    form_data = SkillForm(instance=data)
    context = {
        'form_data': form_data,
        'title': "Update Skill Info",
        'btn_name': 'Update Skill',
    }
    return render(request, 'master/base-form.html',context)

def delete_skill(request, id):
    SkillModel.objects.get(id = id).delete()
    return redirect('skill_list')

def experience_list(request):
    experience_data = ExperienceModel.objects.all()
    
    context = {
        'experience_data': experience_data
    }
    
    return render(request, 'experience-list.html',context)


def add_experience(request):
    if request.method == 'POST':
        form_data = ExprienceForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('experience_list')
    
    form_data = ExprienceForm()
    context = {
        'form_data': form_data,
        'title': "Add Experience Info",
        'btn_name': 'Add Experience',
    }
    return render(request, 'master/base-form.html',context)

def edit_experience(request, id):
    data = ExperienceModel.objects.get(id = id)
    if request.method == 'POST':
        form_data = ExprienceForm(request.POST, instance=data)
        if form_data.is_valid():
            form_data.save()
            return redirect('experience_list')
    
    form_data = ExprienceForm(instance=data)
    context = {
        'form_data': form_data,
        'title': "Update Experience Info",
        'btn_name': 'Update Experience',
    }
    return render(request, 'master/base-form.html',context)

def delete_experience(request, id):
    ExperienceModel.objects.get(id = id).delete()
    return redirect('experience_list')