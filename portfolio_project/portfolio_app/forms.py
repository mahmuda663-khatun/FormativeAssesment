from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from portfolio_app.models import *

class RegisterForm(UserCreationForm):
    class Meta:
        model = AuthUserInfoModel
        fields = ['username','email','password1','password2']
        
class LoginForm(AuthenticationForm):
    pass

class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = '__all__'
        
class ExprienceForm(forms.ModelForm):
    class Meta:
        model = ExperienceModel
        fields = '__all__'
        
class SkillForm(forms.ModelForm):
    class Meta:
        model = SkillModel
        fields = '__all__'
        
class EducationForm(forms.ModelForm):
    class Meta:
        model = EducationModel
        fields = '__all__'
        
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'