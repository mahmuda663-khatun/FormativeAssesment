
from django.contrib import admin
from django.urls import path
from myapp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('',signupPage,name='signup'),
    path('signin/',signinPage,name='signin'),
    path('signout/',signoutPage,name='signout'),
    path('changepass/',changepassPage,name='changepass'),
    path('Dep_page/',Departmentpage,name='Dep_page'),
    path('Dep_edit/<int:id>/',Dep_editPage,name='Dep_edit'),
    path('Dep_delete/<int:id>/',Dep_deletePage,name='Dep_delete'),
    path('Doctor_page/',DoctorPage,name='Doctor_page'),
    path('Doctor_edit/<int:id>/',Doctor_editPage,name='Doctor_edit'),
    path('Doctor_delete/<int:id>/',Doctor_deletePage,name='Doctor_delete'),
    path('PatientPage/',PatientPage,name='PatientPage'),
    path('PatientEdit/<int:id>/',PatientEditPage,name='PatientEdit'),
    path('PatientDelete/<int:id>/',PatientDeletePage,name='PatientDelete'),
    path('ApointmentPage/',ApointmentPage,name='ApointmentPage'),
    path('ApointmentEdit/<int:id>/',ApointmentEditPage,name='ApointmentEdit'),
    path('ApointmentDelete/<int:id>/',ApointmentDeletePage,name='ApointmentDelete'),
]
