from django.urls import path
from . import views


#html file, url, view for any webpage

urlpatterns = [
    path('',views.home, name='home'),
    #path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('student/',views.student, name='student'),
    path('courses/',views.courses, name='courses'),
    path('professor/',views.professor, name='professor'),
    path('register/',views.register_user, name='register'),
]
