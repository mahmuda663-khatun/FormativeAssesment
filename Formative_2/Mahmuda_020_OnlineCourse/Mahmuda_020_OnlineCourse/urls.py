
from django.contrib import admin
from django.urls import path
from  courseplatform.views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('signout/',signout,name='signout'),
    path('categoryPage/',categoryPage,name='categoryPage'),
    path('categoryEdit/<int:id>/',categoryEdit,name='categoryEdit'),
    path('categoryDelete/<int:id>/',categoryDelete,name='categoryDelete'),
    path('Courselist/',Courselist,name='Courselist'),
    path('CourseAdd/',CourseAdd,name='CourseAdd'),
    path('CourseEdit/<int:id>/',CourseEdit,name='CourseEdit'),
    path('CourseDelete/<int:id>/',CourseDelete,name='CourseDelete'),
    path('Enrollmentlist/',Enrollmentlist,name='Enrollmentlist'),
    path('EnrollmentAdd/',EnrollmentAdd,name='EnrollmentAdd'),
    path('EnrollmentEdit/<int:id>/',EnrollmentEdit,name='EnrollmentEdit'),
    path('EnrollmentDelete/<int:id>/',EnrollmentDelete,name='EnrollmentDelete'),
    path('Course_Reviewlist/',Course_Reviewlist,name='Course_Reviewlist'),
    path('Course_ReviewAdd/',Course_ReviewAdd,name='Course_ReviewAdd'),
    path('Course_ReviewEdit/<int:id>/',Course_ReviewEdit,name='Course_ReviewEdit'),
    path('Course_ReviewDelete/<int:id>/',Course_ReviewDelete,name='Course_ReviewDelete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)