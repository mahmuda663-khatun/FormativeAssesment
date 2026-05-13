from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class AuthUserModel(AbstractUser):
    USER_TYPES=[
        ('Admin', "Admin"),
        ('Recruiter', "Recruiter"),
        ('Seeker', "Seeker"),
    ]
    display_name=models.CharField(max_length=100, null=True)
    user_types=models.CharField(max_length=100, null=True, choices=USER_TYPES)

    def __str__(self):
        return self.username

class RecruiterModel(models.Model):
    user=models.OneToOneField(AuthUserModel, on_delete=models.CASCADE, null=True, related_name="Recruiters")
    company_name=models.CharField(max_length=100, null=True)
    image=models.ImageField(null=True, upload_to="pics")
    phone=models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username
    
class SkillModel(models.Model):
    name = models.CharField(max_length=100, unique=True) #uniquw true ek skill bar jate na ashe

    def __str__(self):
        return self.name
    
    
class SeekerModel(models.Model):
    user=models.OneToOneField(AuthUserModel, on_delete=models.CASCADE, null=True, related_name="Seekers")
    address=models.CharField(max_length=100, null=True)
    image=models.ImageField(null=True, upload_to="pics")
    phone=models.CharField(max_length=100, null=True)
    skills = models.ManyToManyField(SkillModel, blank=True)

    def __str__(self):
        return self.user.username

    
class JobModel(models.Model):
    title=models.CharField(max_length=100, null=True)
    category=models.CharField(max_length=100, null=True)
    no_openings=models.CharField(max_length=100, null=True)
    description=models.TextField(null=True)
    salary=models.DecimalField(max_digits=10, decimal_places=2, null=True)
    address=models.CharField(max_length=100, null=True)
    posted_by=models.ForeignKey(RecruiterModel, on_delete=models.CASCADE, null=True)
    required_skills = models.ManyToManyField(SkillModel, blank=True)
    created_at=models.DateField(auto_now_add=True )
    deadline=models.DateField(null=True )

    def __str__(self):
        return self.title
    
class ApplicationModel(models.Model):
    STATUS=[
        ('Pending', 'Pending'),
        ('Shortlisted', 'Shortlisted'),
        ('Confirm', 'Confirm'),
        ('Rejected', 'Rejected'),
    ]
    apply_by=models.ForeignKey(SeekerModel, on_delete=models.CASCADE, null=True)
    applied_at=models.DateField(auto_now_add=True)
    resume=models.FileField(null=True , upload_to="resume")
    status=models.CharField(max_length=100, null=True, choices=STATUS)
    job=models.ForeignKey(JobModel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.apply_by.user.username}-{self.job.title}"