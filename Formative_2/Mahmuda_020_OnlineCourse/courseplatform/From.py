from django import forms
from courseplatform.models import*

class CourseFrom(forms.ModelForm):
    class Meta:
        model = Course_CreationModel
        fields = '__all__'

class EnrollmentFrom(forms.ModelForm):
    class Meta:
        model = EnrollmentModel
        fields = '__all__'

class Course_ReviewFrom(forms.ModelForm):
    class Meta:
        model = Course_ReviewModel
        fields = '__all__'