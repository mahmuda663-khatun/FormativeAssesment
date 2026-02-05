from django.db import models

class DepartmentModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    
    def __str__(self):
        return f'{self.name}-{self.description}'

    
class EmployeeModel(models.Model):
    name = models.CharField(max_length=200, null=True)
    designation = models.CharField(max_length=200, null=True)
    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE, related_name='employee_dept', null=True)
    image = models.ImageField(upload_to='employee_img', null=True)
    
    def __str__(self):
        return f'{self.name}'
