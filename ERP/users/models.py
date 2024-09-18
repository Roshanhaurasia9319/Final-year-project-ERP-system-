from django.db import models

# Create your models here.

class CalendarEvent(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_holiday = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    roll_number=models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    attendance_status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')],default='Absent')
    
    def __str__(self):
        return self.name +"-------->" + self.attendance_status


class Teachers(models.Model):
    tid=models.IntegerField()
    tname=models.CharField(max_length=50)
    tsubject=models.CharField(max_length=200)
    
    def __str__(self):
        return self.tname + "-->" + str(self.tid)
    
    

class TeacherNotification(models.Model):
    notificationMessage = models.CharField(max_length=500)
    


class Courses(models.Model):
    courseType=models.CharField(max_length=200, default=None)
    def __str__(self):
        return self.courseType
    
class CourseYear(models.Model):
    year = models.IntegerField()
    courseType=models.ForeignKey("Courses", on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return str(self.year) + "-->" + self.courseType.courseType

class Section(models.Model):
      sec=models.CharField(max_length=10)
      year=models.ForeignKey("CourseYear", on_delete=models.CASCADE)  
      courseType=models.ForeignKey("Courses", on_delete=models.CASCADE, default=None)
      def __str__(self):
          return self.sec  +"---->" + self.courseType.courseType
      
    
    