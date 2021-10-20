from django.contrib.admin.decorators import register
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Student_Register
from .forms import StudentForm
# Create your views here.

def home(request):
    return render(request,"studentregister/home.html")

# display all students list
def student_list(request):
    students = Student_Register.objects.all()
    
    context = {
        "students":students
    }
    return render(request, "studentregister/student_list.html",context)

# create a student
def student_form(request):
    form = StudentForm()
    
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    context = {
        "form" : form
    }
    return render(request, "studentregister/student_form.html",context)

# update student form
def student_update(request,id):
    
    student = Student_Register.objects.get(id=id)
    
    form = StudentForm(instance = student)
    
    if request.method == "POST":
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save();
            return redirect("student_list")
        
    context = {
        "student":student,
        "form" : form,
    }
    
    return render(request,"studentregister/student_update.html",context)

# delete student form
def student_delete(request,id):
    
    student = Student_Register.objects.get(id=id)
    
    if request.method == "POST":
        
        student.delete()
        return redirect("student_list")
    
    context = {
        "student":student
    }
    return render(request,"studentregister/student_delete.html",context)