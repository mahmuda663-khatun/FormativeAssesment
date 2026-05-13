from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.db.models import Q
from .models import *
from .forms import *
# Create your views here.


def homePage(request):
    return render(request, "master/home.html")

def signupPage(request):
    if request.method=="POST":
        display_name=request.POST.get('display_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        user_types=request.POST.get('user_types')

        user_exist=AuthUserModel.objects.filter(username=username)
        if user_exist:
            messages.warning(request, 'Username already exist')
            return redirect('signup')
        if password==confirm_password:
            user=AuthUserModel.objects.create_user(
                display_name=display_name,
                username=username,
                email=email,
                password=password,
                user_types=user_types,
            )
            if user:
                if user.user_types == "Seeker":
                    SeekerModel.objects.create(
                        user=user
                    )
                    messages.success(request, "Succesfully Seeker Profile Craeted")
                    return redirect('login')
                else:
                    RecruiterModel.objects.create(
                        user=user
                    )
                    messages.success(request, "Succesfully Recruiter Profile Craeted")
                    return redirect('login')
        messages.warning(request, 'Password Didnt Match')
        return redirect('signup')
    return render(request, "auth/signup.html")

def loginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Succesfully login')
            return redirect('home')
        messages.warning(request, "Invalid credentials")
        return redirect('login')
    return render(request, "auth/login.html")

def logoutPage(request):
    logout(request)
    messages.success(request, "Succesfully logout")
    return redirect('login')


#---profile

def profilePage(request):
    current_user=request.user
    if current_user.user_types == "Seeker":
        data=SeekerModel.objects.get(user=current_user)
    else:
        data=RecruiterModel.objects.get(user=current_user)
    return render(request, "profile/profile.html", {'data':data})

def updateprofile(request):
    current_user=request.user
    if current_user.user_types == "Seeker":
        data=SeekerModel.objects.get(user=current_user)
        form_data=SeekerForms(instance=data)
        if request.method=="POST":
            form_data=SeekerForms(request.POST, request.FILES, instance=data)
            if form_data.is_valid():
                form_data.save()
                return redirect('profile')
    else:
        data=RecruiterModel.objects.get(user=current_user)
        form_data=RecruiterForm(instance=data)
        if request.method=="POST":
            form_data=RecruiterForm(request.POST, request.FILES, instance=data)
            if form_data.is_valid():
                form_data.save()
                return redirect('profile')
    return render(request, "master/form.html", {'form_data':form_data, "title": "Update your profile"})

#---job


def jobPage(request):
    search=request.GET.get('search')
    if search:
        data=JobModel.objects.filter(
            Q(title__icontains=search) |
            Q(category__icontains=search)
        )
    else:
        data=JobModel.objects.all()
    return render(request, "job/job.html", {'data':data})

# def addjobPage(request):
#     current_user=request.user
#     rec=RecruiterModel.objects.get(user=current_user)

#     form_data=Jobform()
#     if request.method=="POST":
#         form_data=Jobform(request.POST)
#         if form_data.is_valid():
#             form_data=form_data.save(commit=False)
#             form_data.posted_by=rec
#             form_data.save()
#             form_data.save_m2m() #mnay to many field skill ase 
#             return redirect('job')
#     return render(request, "master/form.html", {'form_data':form_data, "title":"Post a Job "})

def addjobPage(request):
    current_user = request.user
    rec = RecruiterModel.objects.get(user=current_user)

    form_data = Jobform()
    if request.method == "POST":
        form_data = Jobform(request.POST)
        if form_data.is_valid():
            job = form_data.save(commit=False)  # job = JobModel object
            job.posted_by = rec
            job.save()                         # save main object first
            form_data.save_m2m()               # save ManyToMany from form
            return redirect('job')

    return render(request, "master/form.html", {'form_data': form_data, "title": "Post a Job "})
# def editjobPage(request, id):
#     data=JobModel.objects.get(id=id)   
#     form_data=Jobform(instance=data)
#     if request.method=="POST":
#         form_data=Jobform(request.POST, instance=data)
#         if form_data.is_valid():
#             form_data.save()
#             return redirect('job')
#     return render(request, "master/form.html", {'form_data':form_data, "title":"Edit a Job "})

def editjobPage(request, id):
    job_instance = JobModel.objects.get(id=id)
    form_data = Jobform(instance=job_instance)

    if request.method == "POST":
        form_data = Jobform(request.POST, instance=job_instance)
        if form_data.is_valid():
            # Save main object first
            job = form_data.save(commit=False)
            job.save()
            # Save updated ManyToMany skills
            form_data.save_m2m()
            return redirect('job')

    return render(request, "master/form.html", {'form_data': form_data, "title": "Edit a Job "})



def deletejobPage(request, id):
    JobModel.objects.get(id=id).delete()
    return redirect('job')

#---apply
def applyPage(request):
    user=request.user
    if user.user_types=="Seeker":
        sek=SeekerModel.objects.get(user=user)
        data=ApplicationModel.objects.filter(apply_by=sek)
    else:
        data=ApplicationModel.objects.all()
    return render(request, "apply/apply.html", {'data':data})

def addapplyPage(request, id):
    data=JobModel.objects.get(id=id)
    current_user=request.user
    sek=SeekerModel.objects.get(user=current_user)

    form_data=ApplicantForm()
    if request.method=="POST":
        form_data=ApplicantForm(request.POST, request.FILES)
        if form_data.is_valid():
            form_data=form_data.save(commit=False)
            form_data.apply_by=sek
            form_data.job=data
            form_data.status="Pending"
            form_data.save()
            return redirect('apply')
    return render(request, "master/form.html", {'form_data':form_data, "title":"Apply on: ", 'data':data})

def editapplyPage(request):
    return render(request, "master/form.html")

def deleteapplyPage(request, id):
    ApplicationModel.objects.get(id=id).delete()
    return redirect('apply')


#--applicantt+ status

def applicantPage(request, id):
    job_list=JobModel.objects.get(id=id)
    recieve=ApplicationModel.objects.filter(job=job_list)
    return render(request, "apply/applicant.html", {'recieve':recieve})

def changestatus(request, id):
    data=ApplicationModel.objects.get(id=id)

    if data.status == "Pending":
        data.status="Shortlisted"
    elif data.status == "Shortlisted":
        data.status = "Rejected"
    elif data.status == "Rejected":
        data.status = "Confirm"
    data.save()
    return redirect('job')

def matchingjobs(request):
    user = request.user

    if user.user_types != "Seeker":
        return redirect('home')

    seeker = SeekerModel.objects.get(user=user)

    seeker_skills = seeker.skills.all()

    matched_jobs = JobModel.objects.filter(
        required_skills__in=seeker_skills
    ).distinct()
     # Get IDs of jobs already applied to
    applied_jobs = ApplicationModel.objects.filter(apply_by=seeker).values_list('job_id', flat=True)



    return render(request, 'profile/matching.html', {'jobs': matched_jobs, 'applied_jobs': applied_jobs })

