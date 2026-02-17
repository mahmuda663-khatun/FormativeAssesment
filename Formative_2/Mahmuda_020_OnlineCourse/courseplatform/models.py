from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserModel(AbstractUser):
    ROLE=[
        ('Admin','Admin'),
        ('Instructor','Instructor'),
        ('Student','Student'),
    ]
    role=models.CharField(choices=ROLE,max_length=100,null=True)
    full_name=models.CharField(max_length=100,null=True)
    Profile_image=models.ImageField(upload_to='image/', null=True)

    def __str__(self):
        return f'{self.full_name}'
    
class CategoryModel(models.Model):
    category_name=models.CharField(max_length=100,null=True)
    description=models.TextField(null=True)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name
    
class Course_CreationModel(models.Model):
    PUBLISHED=[
        ('Yes','Yes'),
        ('No','No'),
    ]
    instructor=models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True)
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)
    course_title=models.CharField(max_length=100,null=True)
    course_description=models.TextField(null=True)
    course_thumbnail=models.ImageField(upload_to='image/', null=True)
    price=models.IntegerField(null=True)
    is_published=models.CharField(choices=PUBLISHED,max_length=100,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.instructor.username
    
class EnrollmentModel(models.Model):
    student=models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True)
    course=models.ForeignKey(Course_CreationModel,on_delete=models.CASCADE,null=True)
    enrolled_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.username
    
class  Course_ReviewModel(models.Model):
    Rating=[
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    ]
    student=models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True)
    course=models.ForeignKey(Course_CreationModel,on_delete=models.CASCADE,null=True)
    rating=models.CharField(choices=Rating,max_length=100,null=True)
    comment=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.username