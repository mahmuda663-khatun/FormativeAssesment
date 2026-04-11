from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import*
# Create your views here.
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LoginForm(AuthenticationForm):
    pass 

class ProfileForm(forms.ModelForm):
    class Meta:
        model = PorfileModel
        fields = ['name','age','gender','height','weight']
        

class FoodEntryForm(forms.ModelForm):
    class Meta:
        model = FoodEntryModel
        fields = ['item_name','caloris']
