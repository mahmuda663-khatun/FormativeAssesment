from django.urls import path
from .views import *
urlpatterns = [
    path('home/',homePage, name="home"),
    path('',loginPage, name="login"),
    path('logout/',logoutPage, name="logout"),
    path('signup/',signupPage, name="signup"),

    path('profile/',profilePage, name="profile"),
    path('update_profile/',updateprofile, name="updateprofile"),


    path('job/',jobPage, name="job"),
    path('addjob/',addjobPage, name="addjob"),
    path('editjob/<int:id>/',editjobPage, name="editjob"),
    path('deletejob/<int:id>/',deletejobPage, name="deletejob"),

    
    path('apply/',applyPage, name="apply"),
    path('addapply/<int:id>/',addapplyPage, name="addapply"),
    path('editapply/',editapplyPage, name="editapply"),
    path('deleteapply/<int:id>/',deleteapplyPage, name="deleteapply"),


    path('applicant/<int:id>/',applicantPage, name="applicant"),
    path('status/<int:id>/',changestatus, name="status"),


    path('matchingjobs/',matchingjobs, name="matchingjobs"),

]
