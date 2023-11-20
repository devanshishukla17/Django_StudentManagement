from django.contrib import admin

from .models import Courses,Professor,Student,Scores,Taken,Taughtby

# Register your models here.

admin.site.register(Courses)
admin.site.register(Professor)
admin.site.register(Scores)
admin.site.register(Student)
admin.site.register(Taughtby)
admin.site.register(Taken)
