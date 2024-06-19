from django.shortcuts import render
from.models import Student
# Create your views here.
def student_list(request):
    students=Student.objects.all()
    return render(request,'student/students.html',{'students':students})
def view_student(request,id):
    student=Student.objects.get(pk=id)
    return render(request,'student/student_detail.html',{'student':student})