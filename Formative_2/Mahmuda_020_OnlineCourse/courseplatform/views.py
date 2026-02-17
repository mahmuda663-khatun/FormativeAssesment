from django.shortcuts import render,redirect
from courseplatform.models import*
from courseplatform.From import*
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def home(r):
    return render (r,'home.html')

def signup(r):
    if r.method=="POST":
        full_name=r.POST.get('full_name')
        username=r.POST.get('username')
        role=r.POST.get('role')
        email=r.POST.get('email')
        Profile_image=r.FILES.get('Profile_image')
        password=r.POST.get('password')
        confirm_password=r.POST.get('confirm_password')
    
        if confirm_password==password:
            UserModel.objects.create_user(
                full_name=full_name,
                username=username,
                role=role,
                email=email,
                Profile_image=Profile_image,
                password=password,
            )
            return redirect ('signin')

    return render (r,'signup.html')


def signin(r):
    if r.method=="POST":
        username=r.POST.get('username')
        password=r.POST.get('password')
        

        user=authenticate(r,username=username,password=password)
        if user:
            login(r,user)
            messages.success(r,'Successfuly Login')
            return redirect ('home')
        else:
          messages.warning(r,'invalid')
          return redirect('signin')  
        
    return render(r,'signin.html')

def signout(r):
    logout(r)
    return redirect ('signin')

def categoryPage(r):
    C_data=CategoryModel.objects.all()
    if r.method=="POST":
        category_name=r.POST.get('category_name')
        description=r.POST.get('description')
        
        CategoryModel.objects.create(
            category_name=category_name,
            description=description,
        )
    context={
        'C_data':C_data
    }
    return render(r,'categoryPage.html',context)

def categoryEdit(r,id):
    E_data=CategoryModel.objects.get(id=id)
    if r.method=="POST":
        category_name=r.POST.get('category_name')
        description=r.POST.get('description')

        E_data.category_name=category_name
        E_data.description=description
        E_data.save()
        return redirect ('categoryPage')
    context={
        'E_data':E_data
    }
    return render(r,'categoryEdit.html',context)

def categoryDelete(r,id):
    CategoryModel.objects.get(id=id).delete()
    return redirect("categoryPage")

def Courselist(r):
    C_data=Course_CreationModel.objects.all()
    context={
        'C_data':C_data
    }
    return render (r,'Courselist.html',context)

def CourseAdd(r):
    if r.method=='POST':
        course=CourseFrom(r.POST,r.FILES)

        if course.is_valid():
            course.save()
            return redirect('Courselist')
        
    course=CourseFrom()
    context={
        'course':course
    }
    return render (r,'CourseAdd.html',context)

def CourseEdit(r,id):
    C_data=Course_CreationModel.objects.get(id=id)
    if r.method=='POST':
        course=CourseFrom(r.POST,r.FILES,instance=C_data)

        if course.is_valid():
            course.save()
            return redirect('Courselist')
        
    course=CourseFrom(instance=C_data)
    context={
        'course':course
    }
    return render (r,'CourseAdd.html',context)

def CourseDelete(r,id):
    Course_CreationModel.objects.get(id=id).delete()
    return redirect("Courselist")

def Enrollmentlist(r):
    C_data=EnrollmentModel.objects.all()
    context={
        'C_data':C_data
    }
    return render (r,'Enrollmentlist.html',context)

def EnrollmentAdd(r):
    if r.method=='POST':
        course=EnrollmentFrom(r.POST)

        if course.is_valid():
            course.save()
            return redirect('Enrollmentlist')
        
    course=EnrollmentFrom()
    context={
        'course':course
    }
    return render (r,'EnrollmentAdd.html',context)

def EnrollmentEdit(r,id):
    C_data=EnrollmentModel.objects.get(id=id)
    if r.method=='POST':
        course=EnrollmentFrom(r.POST,instance=C_data)

        if course.is_valid():
            course.save()
            return redirect('Enrollmentlist')
        
    course=EnrollmentFrom(instance=C_data)
    context={
        'course':course
    }
    return render (r,'EnrollmentAdd.html',context)

def EnrollmentDelete(r,id):
    EnrollmentModel.objects.get(id=id).delete()
    return redirect("Enrollmentlist")

def Course_Reviewlist(r):
    C_data=Course_ReviewModel.objects.all()
    context={
        'C_data':C_data
    }
    return render (r,'Course_Reviewlist.html',context)

def Course_ReviewAdd(r):
    if r.method=='POST':
        course=Course_ReviewFrom(r.POST)

        if course.is_valid():
            course.save()
            return redirect('Course_Reviewlist')
        
    course=Course_ReviewFrom()
    context={
        'course':course
    }
    return render (r,'Course_ReviewAdd.html',context)

def Course_ReviewEdit(r,id):
    C_data=Course_ReviewModel.objects.get(id=id)
    if r.method=='POST':
        course=Course_ReviewFrom(r.POST,instance=C_data)

        if course.is_valid():
            course.save()
            return redirect('Course_Reviewlist')
        
    course=Course_ReviewFrom(instance=C_data)
    context={
        'course':course
    }
    return render (r,'Course_ReviewAdd.html',context)

def Course_ReviewDelete(r,id):
    Course_ReviewModel.objects.get(id=id).delete()
    return redirect("Course_Reviewlist")