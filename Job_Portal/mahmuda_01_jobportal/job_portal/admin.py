from django.contrib import admin
from job_portal.models import*
# Register your models here.
admin.site.register ([AuthUserModel,Recruiters_profileModel,Seeker_profileModel,Job_PostModel,Job_ApplyingModel])
