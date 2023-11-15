from django.contrib import admin

from .models import Courses,Professor,Student

# Register your models here.

admin.site.register(Courses)
admin.site.register(Professor)

admin.site.register(Student)
