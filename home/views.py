from django.shortcuts import render
from .models import Student

# Create your views here.
# Views are functions or classes that handle requests and return responses
def home(request):
    students=Student.objects.filter(age__gt=22).order_by('name')
    students1=Student.objects.count()
    return render(request,'home/index.html', {'students':students,
    'students_count': students1
    })
