from django.shortcuts import render,redirect
from form_app.models import*
from form_app.Forms import*
# Create your views here.
def home(r):
    
    return render (r,'home.html')

def dep_list(r):
    data=DepartmentModel.objects.all()

    context={
        'data':data
    }
    return render(r,'dep_list.html',context)

def departmentAdd(r):
    if r.method=='POST':
        D_data=DepartmentFrom(r.POST)

        if D_data.is_valid():
            D_data.save()
            return redirect('dep_list')

    else:
       D_data= DepartmentFrom()

    context={
        'from':D_data
    }
    return render (r,'Dep_Add.html',context)

def departmentEdit(r,id):
    E_data=DepartmentModel.objects.get(id=id)
    if r.method=='POST':
        D_data=DepartmentFrom(r.POST,instance=E_data)

        if D_data.is_valid():
            D_data.save()
            return redirect('dep_list')

    else:
       D_data= DepartmentFrom(instance=E_data)

    context={
        'from':D_data
    }

    return render(r,'Dep_Add.html',context)

def departmentdelete(r,id):
    DepartmentModel.objects.get(id=id).delete()
    return redirect(dep_list)


def departmentbd(req):
    data=DepartmentModel.objects.all()
    if req.method=='POST':
        D_data=DepartmentFrom(req.POST)

        if D_data.is_valid():
            D_data.save()
            return redirect('departmentbd')

    else:
       D_data= DepartmentFrom()

    context={
        'from':D_data,
        'data':data
    }
    return render (req,'Dep_page.html',context)