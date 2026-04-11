from django import forms
from caleory_app.models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'
        exclude = ['user','bmr']
    
class CalorieForm(forms.ModelForm):
    class Meta:
        model = CaleoryConsumedModel
        fields = ['item_name','caleory_consumed']