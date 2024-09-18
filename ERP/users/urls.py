from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teacher_dashboard', views.teacher_dashboard, name='teacher_dashboard'),
    path('calendar-data/', views.calendar_view, name='calendar_data'),
    path('markAttendance/', views.markAttendance, name='markAttendance'),
    path('student_dashboard', views.student_dashboard, name='student_dashboard'),
    path('post-notification/', views.postNotification, name='postNotification'),
    path('teacherSignin/', views.teacherSignin, name='teacherSignin'),
]