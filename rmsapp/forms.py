from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from rmsapp.models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class CreateUnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'


class AcademicYearForm(forms.ModelForm):
    class Meta:
        model = academicYear
        fields = ['year']

class CreateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class CreateRoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = '__all__'