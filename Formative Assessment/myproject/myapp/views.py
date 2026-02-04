from django.shortcuts import render,redirect
from myapp.models import*
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

@login_required
def home(r):
    return render (r,'home.html')
@login_required
def signup(r):
    if r.method=="POST":
        username=r.POST.get('username')
        email=r.POST.get('email')
        password=r.POST.get('password')
        confirm_password=r.POST.get('confirm_password')

        if confirm_password==password:
            UserModel.objects.create_user(
            username=username,
            email=email,
            password=password,
            role='Admin',
            )
            
        return redirect('signin')
    return render (r,'signup.html')
@login_required
def signin(r):
    if r.method=="POST":
        username=r.POST.get('username')
        password=r.POST.get('password')
        print(username,password)

        user=authenticate(r,username=username,password=password)

        if user:
            login(r,user)
            messages.success(r,'successfully login')
            return redirect('home')
    return render (r,'signin.html')

def signout(r):
    logout(r)
    return redirect('signin')
@login_required
def changepass(r):
    current_user=r.user
    if r.method=="POST":
        current_password=r.POST.get('current_password')
        new_password=r.POST.get('new_password')
        confrim_password=r.POST.get('confrim_password')

        if check_password (current_password,current_user.password):
            
            if new_password==confrim_password:
                current_user.set_password(new_password)
                current_user.save()
                update_session_auth_hash(r,current_user)
                return redirect ('home')
    return render(r,'changepass.html')

def Dep_page(r):
    d_data=DepartmentModel.objects.all()
    if r.method=="POST":
        name=r.POST.get('name')
        location=r.POST.get('location')

        DepartmentModel.objects.create(
            name=name,
            location=location,
        )

    context={
        'data':d_data
    }
    return render (r,'Dep_page.html',context)

def Dep_edit(r,id):
    E_data=DepartmentModel.objects.get(id=id)
    if r.method=="POST":
        name=r.POST.get('name')
        location=r.POST.get('location')

        E_data.name=name
        E_data.location=location
        E_data.save()
        return redirect('Dep_page')
    context={
        'data':E_data
    }
    return render (r,'Dep_edit.html',context)

def Dep_delete(r,id):
    DepartmentModel.objects.get(id=id).delete()
    return redirect('Dep_page')

def DoctorPage(r):
    d_data=DoctorModel.objects.all()
    dep_data=DepartmentModel.objects.all()
    if r.method=="POST":
        name=r.POST.get('name')
        specialization=r.POST.get('specialization')
        phone=r.POST.get('phone')
        email=r.POST.get('email')
        department=r.POST.get('department')

        dep=DepartmentModel.objects.get(id=department)

        DoctorModel.objects.create(
            name=name,
            specialization=specialization,
            phone=phone,
            email=email,
            department=dep,
        )

    context={
        'data':d_data,
        'dep':dep_data
    }
    return render (r,'Doctor_page.html',context)

def Doctor_edit(r,id):
    E_data=DoctorModel.objects.get(id=id)
    dep_data=DepartmentModel.objects.all()

    if r.method=="POST":
        name=r.POST.get('name')
        specialization=r.POST.get('specialization')
        phone=r.POST.get('phone')
        email=r.POST.get('email')
        department=r.POST.get('department')

        dep=DepartmentModel.objects.get(id=department)
        E_data.name=name
        E_data.specialization=specialization
        E_data.phone=phone
        E_data.email=email
        E_data.department=dep
        E_data.save()
        return redirect('Doctor_page')
    
    context={
        'data':E_data,
        'dep':dep_data
    }
    return render (r,'Doctor_edit.html',context)

def Doctor_delete(r,id):
    DoctorModel.objects.get(id=id).delete()
    return redirect('Doctor_page')

def PatientPage(r):
    p_data=PatientModel.objects.all()
    d_data=DoctorModel.objects.all()

    if r.method=="POST":
        name=r.POST.get('name')
        age=r.POST.get('age')
        gender=r.POST.get('gender')
        phone=r.POST.get('phone')
        address=r.POST.get('address')
        doctor=r.POST.get('doctor')

        doc=DoctorModel.objects.get(id=doctor)

        PatientModel.objects.create(
            name=name,
            age=age,
            gender=gender,
            phone=phone,
            address=address,
            doctor=doc,
        )

    context={
        'F_data':d_data,
        'data':p_data
    }
    return render (r,'PatientPage.html',context)

def PatientEdit(r,id):
    d_data=DoctorModel.objects.all()
    E_data=PatientModel.objects.get(id=id)

    if r.method=="POST":
        name=r.POST.get('name')
        age=r.POST.get('age')
        gender=r.POST.get('gender')
        phone=r.POST.get('phone')
        address=r.POST.get('address')
        doctor=r.POST.get('doctor')

        doc=DoctorModel.objects.get(id=doctor)

        E_data.name=name
        E_data.age=age
        E_data.gender=gender
        E_data.phone=phone
        E_data.address=address
        E_data.doctor=doc
        E_data.save()
        return redirect ('PatientPage')
    context={
        'F_data':d_data,
        'data':E_data
    }
    return render (r,'PatientEdit.html',context)

def PatientDelete(r,id):
    PatientModel.objects.get(id=id).delete()
    return redirect('PatientPage')

def ApointmentPage(r):
    A_data=AppointmentModel.objects.all()
    P_data=PatientModel.objects.get(id=id)
    D_data=DoctorModel.objects.get(id=id)

    if r.method=="POST":
        patient=r.POST.get('patient')
        doctor=r.POST.get('doctor')
        appointment_date=r.POST.get('appointment_date')
        status=r.POST.get('status')

        patient=PatientModel.objects.get(id=patient)
        doc=DoctorModel.objects.get(id=doctor)

        AppointmentModel.objects.create(
            patient=patient,
            doctor=doc,
            appointment_date=appointment_date,
            status=status,
            
        )

    context={
        'Adata':A_data,
        'Pdata':P_data,
        'Ddata':D_data,
    }
    return render(r,'ApointmentPage.html',context)

def ApointmentEdit(r,id):
    E_data=AppointmentModel.objects.get(id=id)
    P_data=PatientModel.objects.get(id=id)
    D_data=DoctorModel.objects.get(id=id)

    if r.method=="POST":
        patient=r.POST.get('patient')
        doctor=r.POST.get('doctor')
        appointment_date=r.POST.get('appointment_date')
        status=r.POST.get('status')

        patient=PatientModel.objects.get(id=patient)
        doc=DoctorModel.objects.get(id=doctor)

        E_data.patient=patient
        E_data.doctor=doc
        E_data.appointment_date=appointment_date
        E_data.status=status
        E_data.save()
        return redirect ('PatientPage')
    
    context={
        'Edata':E_data,
        'Pdata':P_data,
        'Ddata':D_data,
    }
    return render(r,'ApointmentEdit.html',context)

def ApointmentDelete(r,id):
    AppointmentModel.objects.get(id=id).delete()
    return redirect('ApointmentPage.html')                                                                                   