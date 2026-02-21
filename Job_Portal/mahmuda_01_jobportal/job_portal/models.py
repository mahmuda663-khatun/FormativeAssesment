from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class AuthUserModel(AbstractUser):
    User_Type=[
        ('Recruiters','Recruiters'),
        ('Jobseekers','Jobseekers'),
    ]
    display_name=models.CharField(max_length=100,null=True)
    user_type=models.CharField(choices=User_Type, max_length=100,null=True)

    def __str__(self):
        return f'{self.display_name}'
    
class Recruiters_profileModel(models.Model):
    recuriter = models.OneToOneField(
        AuthUserModel,
        on_delete=models.CASCADE,
        related_name= 'recuriter_profile',
        null=True
        )
    company_name= models.CharField(max_length=100,null=True)
    address = models.TextField(null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='image/',null=True)

    def __str__(self):
        return f'{self.company_name}'
    
class Seeker_profileModel(models.Model):
    seeker = models.OneToOneField(
        AuthUserModel,
        on_delete=models.CASCADE,
        related_name= 'Seeker_profile',
        null=True
        )
    contact_number=models.CharField(max_length=11,null=True)
    skill_set = models.TextField(null=True)
    resume = models.FileField(upload_to='Files/',null=True)

    def __str__(self):
        return f'{self.seeker.display_name}'
    
class Job_PostModel(models.Model):
    posted_by =  models.ForeignKey(
        AuthUserModel,
        on_delete=models.CASCADE,
        related_name= 'job_post',
        null=True
        )
    Title = models.CharField(max_length=100,null=True)
    openings = models.IntegerField (null=True)
    Category = models.CharField(max_length=100,null=True)
    Job_description = models.TextField(null=True)
    skills_set= models.TextField(null=True)
    is_published = models.BooleanField(default=True, null=True)
    deadline = models.DateField (null=True)
    posted_at= models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return f'{self.Title}'
    
class Job_ApplyingModel(models.Model):
    STATUS = [
        ('Pending','Pending'),
        ('Confirmed','Confirmed'),
        ('Rejected','Rejected'),
    ]
    applicant = models.ForeignKey(
        AuthUserModel,
        on_delete=models.CASCADE,
        related_name= 'job_applying',
        null=True
        )
    job = models.ForeignKey(
        Job_PostModel,
        on_delete=models.CASCADE,
        related_name= 'job_applying',
        null=True
        )
    applied_at = models.DateField(auto_now_add=True,null=True)
    status = models.CharField(choices=STATUS, max_length=100,null=True)

    def __str__(self):
        return f'{self.applicant.display_name}-{self.job.Title}'