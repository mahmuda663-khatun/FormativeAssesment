from django.contrib import admin
from myapp.models import*
# Register your models here.
admin.site.register(UserModel)
admin.site.register(DepartmentModel)
admin.site.register(DoctorModel)
admin.site.register(PatientModel)
admin.site.register(AppointmentModel)