
from django.contrib import admin
from django.urls import path
from myapp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('signout/',signout,name='signout'),
    path('changepass/',changepass,name='changepass'),
    path('Dep_page/',Dep_page,name='Dep_page'),
    path('Dep_edit/<int:id>/',Dep_edit,name='Dep_edit'),
    path('Dep_delete/<int:id>/',Dep_delete,name='Dep_delete'),
    path('Doctor_page/',DoctorPage,name='Doctor_page'),
    path('Doctor_edit/<int:id>/',Doctor_edit,name='Doctor_edit'),
    path('Doctor_delete/<int:id>/',Doctor_delete,name='Doctor_delete'),
    path('PatientPage/',PatientPage,name='PatientPage'),
    path('PatientEdit/<int:id>/',PatientEdit,name='PatientEdit'),
    path('PatientDelete/<int:id>/',PatientDelete,name='PatientDelete'),
    path('ApointmentPage/',ApointmentPage,name='ApointmentPage'),
    path('ApointmentEdit/<int:id>/',ApointmentEdit,name='ApointmentEdit'),
    path('ApointmentDelete/<int:id>/',ApointmentDelete,name='ApointmentDelete'),
]
