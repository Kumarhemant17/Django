from django.shortcuts import render
from .models import Student

def home(request):
    # Filter students age > 22
    students = Student.objects.filter(age__gt=22).order_by('name')
    
    # Optimized count (uses same queryset)
    students_count = students.count()
    
    # All students ordered by name
    student_name = Student.objects.order_by('name')

    return render(request, 'home/index.html', {
        'students': students,
        'students_count': students_count,
        'student_name': student_name
    })