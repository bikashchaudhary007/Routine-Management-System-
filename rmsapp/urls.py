from django.urls import path
from rmsapp import views
urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('register/',views.registerPage, name="register"),
    path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path('student/',views.studentRoutine, name="student"),
    path('student_details/',views.studentDetails, name="student_details"),
    path('update_student_details/<str:pk>/',views.updateStudentDetails, name="update_student_details"),
    path('course/',views.course, name="course"),
    path('update_course/<str:pk>/',views.updateCourse, name="update_course"),
    path('units/',views.units, name="units"),
    path('update_units/<str:pk>/',views.updateUnits, name="update_units"),
    path('academicYear/',views.Year, name="academicYear"),
    path('update_year/<str:pk>/',views.updateYear, name="update_year"),
    path('teachers/',views.teachers, name="teachers"),
    path('update_teacher/<str:pk>/',views.updateTeacher, name="update_teacher"),
    path('delete_teacher/<str:pk>/',views.deleteTeacher, name="delete_teacher"),
    path('routine/',views.routine, name="routine"),
     path('update_routine/<str:pk>/',views.updateRoutine, name="update_routine"),
     
]