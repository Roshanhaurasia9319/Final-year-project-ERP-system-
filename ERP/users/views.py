from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import CalendarEvent, Student, TeacherNotification, Teachers

# Create your views here.
def index(request):
    
    return render(request, 'users/index.html')

def teacherSignin(request):
    if request.method == "POST":
        Username=request.POST.get('Username')
        Password=request.POST.get('Password')
        
        if Teachers.objects.filter(tname=Username):
            if(Password=="welcome1"):
                teacher = Teachers.objects.get(tname=Username)
                request.session['teacher_data']={
                     'tname' : Username,
                     'tid' : teacher.tid,
                     'tsubject' : teacher.tsubject
                }
                # print(request.session.get('teacher_data'))
                context={
                    'data' : request.session.get('teacher_data')
                }
                return render(request, 'users/teacher_dashboard.html', context)
            else:
                return HttpResponse("Invalid Password")
            
        else:
            return HttpResponse('Invalid username')
        
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


def markAttendance(request):
    if request.method == 'POST':
        for student_id, attendance_status in request.POST.items():
            if student_id.startswith('attendance_'):
                student_id = student_id.replace('attendance_', '')
                student = Student.objects.get(id=student_id)
                student.attendance_status = attendance_status
                student.save()
        return redirect('markAttendance')  # Redirect to the same page after submitting

    students = Student.objects.all()
    return render(request, 'users/markAttendance.html', {'students':students})


def student_dashboard(request):
    Notice = TeacherNotification.objects.all()
    context={
        'Notice':Notice
    }
    return render(request, 'users/student_dashboard.html', context)

def postNotification(request):
    if request.method == "POST":
        notice = request.POST.get('notice')  # Get the notice content from the form
        
        if notice:
            # You can save the notice in the database or perform any other action here
            # For now, let's just return the notice as an HttpResponse
            # return HttpResponse(f"Notification posted: {notice}")
            newNotice = TeacherNotification( notificationMessage=notice)
            newNotice.save()
            return redirect(teacher_dashboard)
        else:
            return HttpResponse("No notice entered.")
    
    return render(request, 'users/teacher_dashboard.html')  # Replace 'notification_form.html' with your actual template
         
        

# # List of student data
# students_data = [
#     {'name': 'Roshan', 'roll_number': 6, 'attendance_status': 'Absent'},
#     {'name': 'John Doe', 'roll_number': 7, 'attendance_status': 'Absent'},
#     {'name': 'Jane Smith', 'roll_number': 8, 'attendance_status': 'Absent'},
#     # Add more student data here
# ]

# # Create a list of Student instances
# student_objects = [Student(name=data['name'], roll_number=data['roll_number'], attendance_status=data['attendance_status']) for data in students_data]

# # Bulk create the data
# Student.objects.bulk_create(student_objects)