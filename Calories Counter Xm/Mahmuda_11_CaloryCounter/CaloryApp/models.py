from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class PorfileModel(models.Model):
    Gender=[
        ('Male','Male'),
        ('Female','Female')
    ]
    User = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    name= models.CharField(max_length=100)
    age=models.IntegerField(null=True)
    gender=models.CharField(max_length=100,choices=Gender,null=True)
    height = models.FloatField(help_text="Height in cm")
    weight = models.FloatField(help_text="weight in kg")
    bmr=models.FloatField(null=True,blank=True)

    # def __str__(self):
    #     return f"{self.user.username}"
    
class FoodEntryModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item_name=models.CharField(max_length=100,null=True)
    caloris = models.IntegerField(null=True)
    date=models.DateField(default=timezone.now)

    # def __str__(self):
    #     return f"{self.item_name} - {self.caloris} kcal on {self.data}"
