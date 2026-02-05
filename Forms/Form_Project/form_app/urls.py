
from django.urls import path
from form_app.views import*

urlpatterns = [
    path('',home,name='home'),
    path('dep_list/',dep_list,name='dep_list'),
    path('departmentAdd/',departmentAdd,name='departmentAdd'),
    path('departmentEdit/<int:id>',departmentEdit,name='departmentEdit'),
    path('departmentdelete/<int:id>',departmentdelete,name='departmentdelete'),
    path('departmentbd/',departmentbd,name='departmentbd'),
    
]
