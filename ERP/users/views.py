from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from .models import CalendarEvent

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def teacher_dashboard(request):
    return render(request, 'users/teacher_dashboard.html')



def calendar_view(request):
    events = CalendarEvent.objects.all()
    events_list = []
    for event in events:
        events_list.append({
            'title': event.title,
            'start': event.start_date.isoformat(),
            'end': event.end_date.isoformat() if event.end_date else None,
            'description': event.description,
            'isHoliday': event.is_holiday
        })
    return JsonResponse(events_list, safe=False)
