from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from .forms import *
from rmsapp.models import Course
from rmsapp.models import Unit
from rmsapp.models import academicYear

# Create your views here.
def home(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def registerPage(request):
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'dashboard/register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request, user)
            return redirect('student')
        else:
            messages.info(request, 'username or password is incorrect')
    context={}
    
    return render(request, 'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')
    
def student(request):
    return render(request, 'student.html')

def course(request):
    form = CreateCourseForm()
    if request.method=='POST':
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            form.save()

    courses = Course.objects.all() 
    context={'form': form,'courses': courses}
    return render(request, 'dashboard/course.html', context )

def units(request):
    form = CreateUnitForm()
    if request.method=='POST':
        form = CreateUnitForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('units')
            
    
    units = Unit.objects.all()
    context={'form': form, 'units': units} 
    return render(request, 'dashboard/units.html',context)

def Year(request):
    form = AcademicYearForm()
    if request.method == 'POST':
        form = AcademicYearForm(request.POST)
        if form.is_valid():
            form.save()
    
    years = academicYear.objects.all() 
    context={'form': form, 'years':years}
    return render(request, 'dashboard/academicYear.html', context)

#Creating view for teachers
def teachers(request):
    form = CreateTeacherForm()
    if request.method == 'POST':
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    
    teachers = Teacher.objects.all() 
    context={'form': form, 'teachers':teachers}
    return render(request, 'dashboard/teachers.html', context)

#Creating updateTeacher View
def updateTeacher(request, pk):
    teacher = Teacher.objects.get(id=pk)
    form = CreateTeacherForm(instance=teacher)
    if request.method == 'POST':
        form = CreateTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    teachers = Teacher.objects.filter(id=pk)
    context={'form': form, 'teachers':teachers}
    return render(request, 'dashboard/teachers.html', context)

#Creating deleteTeacher view
def deleteTeacher(request,pk):
    teacher = Teacher.objects.get(id=pk)
    if request.method=="POST":
        teacher.delete()
        return redirect('teachers')
    context={'teacher': teacher}
    return render(request, 'dashboard/deleteTeacher.html', context)


#Creating views for routine
def routine(request):
    form = CreateRoutineForm()
    if request.method == 'POST':
        form = CreateRoutineForm(request.POST)
        if form.is_valid():
            form.save()
    
    routines = Routine.objects.all() 
    context={'form': form, 'routines':routines}
    return render(request, 'dashboard/routine.html', context)

    


