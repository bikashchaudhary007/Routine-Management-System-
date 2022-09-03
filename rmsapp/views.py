from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from rmsapp.decorators import *
from django.contrib.auth.models import Group
from .forms import CreateUserForm
from .forms import *
from rmsapp.models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

@login_required(login_url='login')
@admin_only
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            useremail = request.POST.get('email')
            group = Group.objects.get(name='student')
            user.groups.add(group)

            Student.objects.create(
                user=user,
                name = username,
                email = useremail,
            )
            return redirect('student_details')
            messages.success(request, 'Account was created for ' + username)

    context = {'form':form}
    return render(request, 'dashboard/register.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'username or password is incorrect')
    context={}
    
    return render(request, 'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

#Creating studentRoutine view
@login_required(login_url='login') 
@allowed_users(allowed_roles=['student'])   
def studentRoutine(request):
    user = request.user
    student = Student.objects.get(user=user)
    stdYear = student.year
    stdLevel = student.level
    stdSemester = student.semester
    print('User:',user, '\nstudent: ',student, '\nYear: ', stdYear, 
    '\nLevel: ',stdLevel, '\nsemester: ', stdSemester)
    routines = Routine.objects.filter(year=stdYear, level=stdLevel, semester=stdSemester)
    context={'routines': routines}
    return render(request, 'dashboard/student.html', context)

#Creating course view
@login_required(login_url='login')  
@allowed_users(allowed_roles=['admin']) 
def course(request):
    form = CreateCourseForm()
    if request.method=='POST':
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course')
    courses = Course.objects.all() 
    context={'form': form,'courses': courses}
    return render(request, 'dashboard/course.html', context )

#Creating updateCourse view
@login_required(login_url='login') 
@allowed_users(allowed_roles=['admin'])  
def updateCourse(request,pk):
    course = Course.objects.get(id=pk)
    form = CreateCourseForm(instance=course)
    if request.method=='POST':
        form = CreateCourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course')

    courses = Course.objects.filter(id=pk)
    context={'form': form,'courses': courses}
    return render(request, 'dashboard/course.html', context )

#Creating units views
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])   
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

#Creating updateUnits view
@login_required(login_url='login')  
@allowed_users(allowed_roles=['admin']) 
def updateUnits(request,pk):
    unit = Unit.objects.get(id=pk)
    form = CreateUnitForm(instance=unit)
    if request.method=='POST':
        form = CreateUnitForm(request.POST,instance=unit)
        if form.is_valid():
            form.save()  
            return redirect('units')
    
    units = Unit.objects.filter(id=pk)
    context={'form': form, 'units': units} 
    return render(request, 'dashboard/units.html',context)

#Creating Academic Year View
@login_required(login_url='login')  
@allowed_users(allowed_roles=['admin']) 
def Year(request):
    form = AcademicYearForm()
    if request.method == 'POST':
        form = AcademicYearForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('academicYear')
    
    years = academicYear.objects.all() 
    context={'form': form, 'years':years}
    return render(request, 'dashboard/academicYear.html', context)

#Creating updateYear view
@login_required(login_url='login')   
@allowed_users(allowed_roles=['admin'])
def updateYear(request,pk):
    year = academicYear.objects.get(id=pk)
    form = AcademicYearForm(instance=year)
    if request.method == 'POST':
        form = AcademicYearForm(request.POST, instance=year)
        if form.is_valid():
            form.save()
            return redirect('academicYear')
    
    years = academicYear.objects.filter(id=pk) 
    context={'form': form, 'years':years}
    return render(request, 'dashboard/academicYear.html', context)

#Creating view for teachers
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])   
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
@login_required(login_url='login')   
@allowed_users(allowed_roles=['admin'])
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
@login_required(login_url='login') 
@allowed_users(allowed_roles=['admin'])  
def deleteTeacher(request,pk):
    teacher = Teacher.objects.get(id=pk)
    if request.method=="POST":
        teacher.delete()
        return redirect('teachers')
    context={'teacher': teacher}
    return render(request, 'dashboard/deleteTeacher.html', context)


#Creating views for routine
@login_required(login_url='login')   
@allowed_users(allowed_roles=['admin'])
def routine(request):
    form = CreateRoutineForm()
    if request.method == 'POST':
        form = CreateRoutineForm(request.POST)
        if form.is_valid():
            form.save()
    
    routines = Routine.objects.all() 
    context={'form': form, 'routines':routines}
    return render(request, 'dashboard/routine.html', context)


#Creating Student Details
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def studentDetails(request):
    form = CreateStudentFrom()
    if request.method=='POST':
        form = CreateStudentFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_details')
    students = Student.objects.all() 
    context={'form': form,'students': students}
    return render(request, 'dashboard/studentDetails.html', context )

#Creating updateStudentDetails view
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateStudentDetails(request, pk):
    student = Student.objects.get(id=pk)
    form = CreateStudentFrom(instance=student)
    if request.method=='POST':
        form = CreateStudentFrom(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_details')

    students = Student.objects.filter(id=pk)
    context={'form': form,'students': students}
    return render(request, 'dashboard/studentDetails.html', context )





#Creating updateRoutine view
@login_required(login_url='login')  
@allowed_users(allowed_roles=['admin']) 
def updateRoutine(request,pk):
    routine = Routine.objects.get(id=pk) 
    form = CreateRoutineForm(instance=routine)
    if request.method == 'POST':
        form = CreateRoutineForm(request.POST,instance=routine)
        if form.is_valid():
            form.save()
            return redirect('routine')
    
    routines = Routine.objects.filter(id=pk)
    context={'form': form, 'routines':routines}
    return render(request, 'dashboard/routine.html', context)





    


