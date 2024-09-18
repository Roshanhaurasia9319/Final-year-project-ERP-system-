from django.contrib import admin
from .models import CalendarEvent, Student, TeacherNotification, Teachers, CourseYear, Courses, Section

# Register your models here.
admin.site.register(CalendarEvent)
admin.site.register(Student)
admin.site.register(TeacherNotification)
admin.site.register(Teachers)
admin.site.register(Courses)
admin.site.register(CourseYear)
admin.site.register(Section)
