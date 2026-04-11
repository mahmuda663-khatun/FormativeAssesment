from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    height = models.FloatField(help_text="Height in cm")
    weight = models.FloatField(help_text="Weight in kg")
    bmr = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Calculate BMR based on gender
        # Male: BMR = 66.47 + (13.75 × weight) + (5.003 × height) − (6.755 × age)
        # Female: BMR = 655.1 + (9.563 × weight) + (1.850 × height) − (4.676 × age)
        if self.gender == 'Male':
            self.bmr = 66.47 + (13.75 * self.weight) + (5.003 * self.height) - (6.755 * self.age)
        else:
            self.bmr = 655.1 + (9.563 * self.weight) + (1.850 * self.height) - (4.676 * self.age)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class FoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    calories = models.IntegerField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.item_name} - {self.calories} kcal on {self.date}"
