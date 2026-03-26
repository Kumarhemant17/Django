from django.shortcuts import render
from .models import Student

def home(request):
    students = Student.objects.filter(age__gt=22).order_by('name')
    students_count = students.count()   # improved
    student_name = Student.objects.order_by('name')

    return render(request, 'home/index.html', {
        'students': students,
        'students_count': students.count(),
        'student_name': all_students
    })