from django.urls import path
from job_portal.views import*

urlpatterns = [
    path('home/',home,name='home'),
    path('',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('signout/',signout,name='signout'),
]