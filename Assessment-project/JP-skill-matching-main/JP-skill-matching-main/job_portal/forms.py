from django import forms
from .models import *

class SeekerForms(forms.ModelForm):
    class Meta:
        model=SeekerModel
        fields="__all__"
        widgets={
            'skills': forms.CheckboxSelectMultiple()
        }
        exclude=['user']

        
class RecruiterForm(forms.ModelForm):
    class Meta:
        model=RecruiterModel
        fields="__all__"
        exclude=['user']


class Jobform(forms.ModelForm):
    class Meta:
        model=JobModel
        fields="__all__"
        widgets={
            "deadline":forms.DateInput(attrs={'type':'date'}),
            'skills': forms.CheckboxSelectMultiple()
        }
        exclude=['posted_by']


class ApplicantForm(forms.ModelForm):
    class Meta:
        model=ApplicationModel
        fields="__all__"
        exclude=['apply_by', 'status', 'job']