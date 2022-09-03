from django.db import models
from django.contrib.auth.models import User

# Create your models here.




#Create staff model



#Creating model for course
class Course(models.Model):
    courseCode = models.CharField(max_length=50)
    courseName = models.CharField(max_length=200)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.courseName

class Unit(models.Model):
    level = (
        ('4','4'),
        ('5','5'),
        ('6','6'),
    )
    unitCode = models.CharField(max_length=50)
    unitLevel = models.CharField(max_length=50, null=True, choices=level)
    unitCredits = models.CharField(max_length=50, null=True)
    unitName= models.CharField(max_length=200)
    course = models.ForeignKey(Course, null=True ,on_delete= models.SET_NULL) #CourseID (FK)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.unitName

#Creating Academic Year Model
class academicYear(models.Model):
    year = models.CharField(max_length=50)
    dateCreated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.year

#Creating teacher model
class Teacher(models.Model):
    level = (
        ('4','4'),
        ('5','5'),
        ('6','6'),
    )
    teacherID  = models.CharField(max_length=50)
    teacherName  = models.CharField(max_length=200)
    teacherLevel  = models.CharField(max_length=50, null=True, choices=level)
    course = models.ForeignKey(Course, null=True ,on_delete= models.SET_NULL) #CourseID (FK)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.teacherName

#Create student model 
class Student(models.Model):
    level = (
        ('4','4'),
        ('5','5'),
        ('6','6'),
    )
    sem = (
        ('I','I'),
        ('II','II'),
        ('III','III'),
        ('IV','IV'),
        ('V','V'),
        ('VI','VI'),
    )
    name = models.CharField(max_length=200, null= True)
    email = models.CharField(max_length=200, null= True)
    address = models.CharField(max_length=200, null= True)
    year = models.ForeignKey(academicYear, null=True,blank=True ,on_delete= models.SET_NULL) #Academic Year ID (FK)
    level = models.CharField(max_length=50, null=True, choices=level)
    semester = models.CharField(max_length=50, null=True, choices=sem)
    user = models.ForeignKey(User, null=True, on_delete = models.CASCADE)

    def __str__(self):
        return self.name



class Routine(models.Model):
    days = (
        ('Sun','Sun'),
        ('Mon', 'Mon'),
        ('Tue', 'Tue'),
        ('Wed', 'Wed'),
        ('Thu', 'Thu'),
        ('Fri', 'Fri'),
        ('Sat', 'Sat'),
    )

    levels = (
        ('4','4'),
        ('5','5'),
        ('6','6'),
    )

    sem = (
        ('I','I'),
        ('II','II'),
        ('III','III'),
        ('IV','IV'),
        ('V','V'),
        ('VI','VI'),
    )


    weekdays = models.CharField(max_length=50, null=True, choices=days)
    startTime = models.CharField(max_length=50, null=True)
    endTime = models.CharField(max_length=50, null=True)
    unit = models.ForeignKey(Unit, null=True ,on_delete= models.SET_NULL) #UnitID (FK)
    teacher = models.ForeignKey(Teacher, null=True ,on_delete= models.SET_NULL) #TeacherID (FK)
    level = models.CharField(max_length=50, null=True, choices=levels)
    semester = models.CharField(max_length=50, null=True, choices=sem)
    year = models.ForeignKey(academicYear, null=True ,on_delete= models.SET_NULL) #Academic Year ID (FK)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.weekdays








    