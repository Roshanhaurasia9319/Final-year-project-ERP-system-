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
