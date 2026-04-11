from django.contrib import admin
from django.urls import path
from CaloryApp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',dashboard_view, name='home'),
    path('', register_view, name='register'),
    path('login/',Login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('add-food/',add_food_view, name='add_food'),
    path('dashboard/',dashboard_view, name='dashboard'),
    
]
