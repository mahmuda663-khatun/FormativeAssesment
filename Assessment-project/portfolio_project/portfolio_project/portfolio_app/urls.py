from django.urls import path
from portfolio_app.views import *


urlpatterns = [
    path('register/', register_page, name='register_page'),
    path('login/',login_page,name='login_page'),
    path('logout/',logout_Page,name='logout_Page'),
    path('dashboard/',dashboard,name='dashboard'),
    path('',profile_page,name='profile_page'),
    path('update-profile/',update_profile,name='update_profile'),
    path('resume/',resume_page,name='resume_page'),
    
    path('project-list/',project_list, name='project_list'),
    path('add-project/',add_project,name='add_project'),
    path('edit-project/<int:id>/',edit_project,name='edit_project'),
    path('delete-project/<int:id>/',delete_project,name='delete_project'),
    
    path('skill-list/',skill_list,name='skill_list'),
    path('add-skill/',add_skill,name='add_skill'),
    path('edit-skill/<int:id>/',edit_skill,name='edit_skill'),
    path('delete-skill/<int:id>/',delete_skill,name='delete_skill'),
    
    path('experience-list/',experience_list,name='experience_list'),
    path('add-experience/',add_experience,name='add_experience'),
    path('edit-experience/<int:id>/',edit_experience,name='edit_experience'),
    path('delete-experience/<int:id>/',delete_experience,name='delete_experience'),
]
