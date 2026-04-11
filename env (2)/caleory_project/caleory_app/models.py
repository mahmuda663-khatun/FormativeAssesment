from django.db import models
from django.contrib.auth.models import User

class ProfileModel(models.Model):
    #  Name, Age, Gender, Height, Weight
    GENDER_TYPES = [
        ('Male','Male'),
        ('Female','Female'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='user_profile')
    name = models.CharField(max_length=200, null=True)
    age = models.IntegerField(null=True, help_text='Age in Years')
    gender = models.CharField(choices=GENDER_TYPES, max_length=10, null=True)
    height = models.FloatField(null=True, help_text=' height in cm')
    weight = models.FloatField(null=True, help_text='weight in kg')
    bmr = models.FloatField(null=True)

    def __str__(self):
        return f'{self.user.username}-{self.name}'
    
class CaleoryConsumedModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_caleory_consumed')
    item_name = models.CharField(max_length=200, null=True)
    caleory_consumed = models.FloatField(null=True)
    date = models.DateField(auto_now_add=True, null=True)
    def __str__(self):
        return f'{self.user.username}-{self.item_name}:{self.caleory_consumed}'



