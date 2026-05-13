from django.contrib import admin
from portfolio_app.models import *

admin.site.register([AuthUserInfoModel, ProjectModel, ExperienceModel, EducationModel, SkillModel])