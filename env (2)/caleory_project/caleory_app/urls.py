from django.urls import path
from caleory_app.views import *


urlpatterns = [
    path('',login_function, name='login_function'),
    path('register/',register_function, name='register_function'),
    path('dashboard/',dashboard, name='dashboard'),
    path('logout/',logout_function,name='logout_function'),

    path('profile/',profile_page, name='profile_page'),
    path('update-profile',profile_update,name='profile_update'),

    path('consumed-calories/',consumed_calorie, name='consumed_calorie'),
    path('add-calorie/',add_calorie,name='add_calorie'),
    path('edit-calorie/<int:pk>/',edit_calorie, name='edit_calorie'),
    path('delete-calorie/<int:pk>/',delete_calorie, name='delete_calorie'),
]