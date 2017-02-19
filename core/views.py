from django.shortcuts import render
from .models import Students


def student_list(request):

    students = Students.objects.all()
    return render(request, 'core/student_list.html', {'students': students})

def student_detail(request, pk):

    student_info = Students.objects.get(pk=pk)
    students = Students.objects.all()

    return render(request, 'core/student_info.html',{'student': student_info, 'students': students})
# Create your views here.
