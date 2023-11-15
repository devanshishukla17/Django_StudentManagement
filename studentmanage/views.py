from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Student,Courses,Professor

# Create your views here.

def home(request):
#login page is inside home function cause no one can view webpage without first being logged in

    student_records=Student.objects.all()
    course_records=Courses.objects.all()
    professor_records=Professor.objects.all()

    #check to see if person is logging in
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        #authenticate
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"You have been logged in!")
            return redirect('home')
        else:
            messages.success(request,"ERROR,Please try again...")
            return redirect('home')
        
    else:
        return render(request,'home.html',{'student_records':student_records, 'course_records':course_records, 'professor_records':professor_records})
    


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def register_user(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and login
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have successfully registered...")
            return redirect('home')
    else:
        form=SignUpForm()
        return render(request,'register.html',{'form':form})
    
    return render(request,'register.html',{'form':form})

def student(request):
    student_records=Student.objects.all()
    return render(request,'student.html',{'student_records':student_records})

def courses(request):
    course_records=Courses.objects.all()
    return render(request,'courses.html',{'course_records':course_records})

def professor(request):
    professor_records=Professor.objects.all()
    return render(request,'professor.html',{'professor_records':professor_records})