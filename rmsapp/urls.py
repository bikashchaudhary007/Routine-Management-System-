from django.urls import path
from rmsapp import views
urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('register/',views.registerPage, name="register"),
    path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path('student/',views.student, name="student"),
    path('course/',views.course, name="course"),
    path('units/',views.units, name="units"),
    path('academicYear/',views.Year, name="academicYear"),
    path('teachers/',views.teachers, name="teachers"),
    path('update_teacher/<str:pk>/',views.updateTeacher, name="update_teacher"),
    path('delete_teacher/<str:pk>/',views.deleteTeacher, name="delete_teacher"),
    path('routine/',views.routine, name="routine"),
     
]