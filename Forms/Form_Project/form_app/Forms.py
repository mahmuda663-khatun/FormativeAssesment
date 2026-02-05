from django import forms
from form_app.models import*

class DepartmentFrom(forms.ModelForm):
    class Meta:
        model=DepartmentModel
        fields = '__all__'