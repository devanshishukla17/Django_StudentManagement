# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Courses(models.Model):
    courseid = models.CharField(db_column='CourseID', primary_key=True, max_length=10)  # Field name made lowercase.
    coursename = models.CharField(db_column='CourseName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    semester = models.IntegerField(db_column='Semester', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'courses'

    def __str__(self):
        return f"Course {self.courseid}"


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Professor(models.Model):
    profid = models.IntegerField(db_column='ProfID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=25, blank=True, null=True)  # Field name made lowercase.
    phoneno = models.BigIntegerField(db_column='PhoneNo', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dateofjoining = models.DateField(db_column='DateOfJoining', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'professor'
    
    def __str__(self):
        return f"Professor {self.profid}"


class Scores(models.Model):
    rollno = models.ForeignKey('Student', models.DO_NOTHING, db_column='RollNo', blank=True, null=True)  # Field name made lowercase.
    courseid = models.ForeignKey(Courses, models.DO_NOTHING, db_column='CourseID', blank=True, null=True)  # Field name made lowercase.
    examtype = models.CharField(db_column='ExamType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    grade = models.CharField(db_column='Grade', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'scores'

    def __str__(self):
        return f"Scores - Student: {self.rollno}, Course: {self.courseid}, Exam Type: {self.examtype}, Grade: {self.grade}"


class Student(models.Model):
    rollno = models.IntegerField(db_column='Rollno', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phoneno = models.CharField(db_column='PhoneNo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=40, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    dateofadmission = models.DateField(db_column='DateOfAdmission', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student'

    def __str__(self):
        return f"Student {self.rollno}"


class Taken(models.Model):
    rollno = models.ForeignKey(Student, models.DO_NOTHING, db_column='RollNo', blank=True, null=True)  # Field name made lowercase.
    courseid = models.ForeignKey(Courses, models.DO_NOTHING, db_column='CourseID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taken'


class Taughtby(models.Model):
    profid = models.ForeignKey(Professor, models.DO_NOTHING, db_column='ProfID', blank=True, null=True)  # Field name made lowercase.
    courseid = models.ForeignKey(Courses, models.DO_NOTHING, db_column='CourseID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taughtby'

#new modifications

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Student, Professor, Courses

# View for listing students with pagination
def student_list(request):
    student_list = Student.objects.all()
    paginator = Paginator(student_list, 10)  # Show 10 students per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'students/student_list.html', {'page_obj': page_obj})

# View for listing professors with pagination
def professor_list(request):
    professor_list = Professor.objects.all()
    paginator = Paginator(professor_list, 10)  # Show 10 professors per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'professors/professor_list.html', {'page_obj': page_obj})

# View for listing courses with pagination
def course_list(request):
    course_list = Courses.objects.all()
    paginator = Paginator(course_list, 10)  # Show 10 courses per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'courses/course_list.html', {'page_obj': page_obj})


# TEMPLATES
'''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student List</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    <h1>Students</h1>
    <ul>
        {% for student in page_obj %}
            <li>{{ student.firstname }} {{ student.lastname }} - Roll No: {{ student.rollno }}</li>
        {% endfor %}
    </ul>

    <div class="pagination">
        <span class="step-links">
            {% if page_obj.has_previous %}
                <a href="?page=1">&laquo; first</a>
                <a href="?page={{ page_obj.previous_page_number }}">previous</a>
            {% endif %}

            <span class="current">
                Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
            </span>

            {% if page_obj.has_next %}
                <a href="?page={{ page_obj.next_page_number }}">next</a>
                <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
            {% endif %}
        </span>
    </div>

    <h1>Professors</h1>
    <ul>
        {% for professor in page_obj %}
            <li>{{ professor.name }} - Prof ID: {{ professor.profid }}</li>
        {% endfor %}
    </ul>

    <div class="pagination">
        <span class="step-links">
            {% if page_obj.has_previous %}
                <a href="?page=1">&laquo; first</a>
                <a href="?page={{ page_obj.previous_page_number }}">previous</a>
            {% endif %}

            <span class="current">
                Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
            </span>

            {% if page_obj.has_next %}
                <a href="?page={{ page_obj.next_page_number }}">next</a>
                <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
            {% endif %}
        </span>
    </div>

    <h1>Courses</h1>
    <ul>
        {% for course in page_obj %}
            <li>{{ course.coursename }} - Course ID: {{ course.courseid }}</li>
        {% endfor %}
    </ul>

    <div class="pagination">
        <span class="step-links">
            {% if page_obj.has_previous %}
                <a href="?page=1">&laquo; first</a>
                <a href="?page={{ page_obj.previous_page_number }}">previous</a>
            {% endif %}

            <span class="current">
                Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
            </span>

            {% if page_obj.has_next %}
                <a href="?page={{ page_obj.next_page_number }}">next</a>
                <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
            {% endif %}
        </span>
    </div>
</body>
</html>
'''

#url config
'''

from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('professors/', views.professor_list, name='professor_list'),
    path('courses/', views.course_list, name='course_list'),
]

'''




