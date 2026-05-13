from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([AuthUserModel, RecruiterModel, SeekerModel, JobModel, ApplicationModel, SkillModel])