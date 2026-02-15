from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    students = Student.objects.all()
    return render(request, 'students/home.html', {'students': students})

@login_required
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect('student_home')
    else:
        form = StudentForm()

    return render(request, 'students/add_student.html', {'form': form})

@login_required
def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('student_home')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/edit_student.html', {'form': form})

@login_required
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.success(request, "Student deleted successfully!")
    return redirect('student_home')


