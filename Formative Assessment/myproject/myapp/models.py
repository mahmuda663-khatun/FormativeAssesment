from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserModel(AbstractUser):
    ROLE=[
        ('Admin','Admin'),
        ('Doctor','Doctor'),
        ('Patient','Patient'),
    ]
    role=models.CharField(choices=ROLE,null=True)

    def __str__(self):
        return self.username
    
class DepartmentModel(models.Model):
    name=models.CharField(null=True)
    location=models.CharField(null=True)

    def __str__(self):
        return self.name
    
class DoctorModel(models.Model):
    SPECIALIZATION=[
        ('Cardiology','Cardiology'),
        ('Dermatology','Dermatology'),
        ('Neurology','Neurology')
    ]
    name=models.CharField(null=True)
    specialization=models.CharField(choices=SPECIALIZATION,null=True)
    phone=models.CharField(max_length=11,null=True)
    email=models.EmailField(null=True)
    department=models.ForeignKey(DepartmentModel,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name
    
class PatientModel(models.Model):
    GENDER=[
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]
    name=models.CharField(null=True)
    age=models.IntegerField(null=True)
    gender=models.CharField(choices=GENDER,null=True)
    phone=models.CharField(max_length=11,null=True)
    address=models.TextField(null=True)
    doctor=models.ForeignKey(DoctorModel,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name
    
class AppointmentModel(models.Model):
    STATUS=[
        ('Pending','Pending'),
        ('Completed','Completed'),
        ('Cancelled','Cancelled'),
    ]
    patient=models.ForeignKey(PatientModel,on_delete=models.CASCADE,null=True)
    doctor=models.ForeignKey(DoctorModel,on_delete=models.CASCADE,null=True)
    appointment_date=models.DateTimeField(null=True)
    status=models.CharField(choices=STATUS,null=True)

    def __str__(self):
        return self.patient