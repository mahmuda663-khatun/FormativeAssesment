from django.contrib import admin
from courseplatform.models import*
# Register your models here.
admin.site.register([UserModel,CategoryModel,Course_CreationModel,EnrollmentModel,Course_ReviewModel])