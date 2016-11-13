from django.http import HttpResponse
from django.template import loader
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect,reverse, HttpResponseRedirect
from django.db.models import Q
from .forms import UserForm

'''def index(request):
    return HttpResponse("<h1>This is index app homepage</h1>")'''



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        print role
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #print 'stud1'
                login(request, user)
                #print role+'1'
                role = str(role)
                #print type(Student.webmail)
                if role == "Student":
                    student = Student.objects.get(webmail=username)
                    return redirect('/stud_profile')
                elif role == "Library":
                    pass
            else:
                return render(request, 'main/login.html', {'error_message': 'Unsuccessful Login'})
        else:
            return render(request, 'main/login.html', {'error_message': 'Invalid login'})
    return render(request, 'main/login.html',{'error_message': 'Valid login it was!'})

def stud_profile(request):
    username=request.user.username
    username=str(username)
    student = Student.objects.get(webmail=username)
    return render(request, 'main/stud.html', {'error_message': 'valid login', 'student': student})


def stud_full_dept(request):
    username = request.user.username
    username=str(username)
    student = Student.objects.get(webmail=username)
    faculty_dept = Faculty.objects.filter(department=student.department)
    stud_fac_status = Stud_Faculty_Status.objects.filter(student=student)
    return render(request, 'main/stud_full_dept.html', {'error_message': 'valid login', 'student': student, 'faculty':faculty_dept,'Stud_Faculty_Status':stud_fac_status})


def stud_full_lab(request):
    username = request.user.username
    username = str(username)
    student = Student.objects.filter(webmail=username)
    labs = Lab.objects.all()
    stud_lab_status = Stud_Lab_Status.objects.filter(student=student)
    return render(request, 'main/stud_full_lab.html', {'error_message': 'valid login', 'student': student, 'labs' : labs, 'Stud_Lab_Status':stud_lab_status})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'main/login.html', context)

def faculty_admin(request):
    username=request.user.username
    faculty = Faculty.objects.get(webmail=username)
    stud_fac_status = Stud_Faculty_Status.objects.filter(faculty=username)
    for i in stud_fac_status :
        Stud_Faculty_Status.objects.get(faculty=username,student=i.student).faculty_approval=request.POST[i.student]

def library_admin(request):
    username = request.user.username
    #take inputs of user by request.POST
    if request.method == "POST":
        for i in Student:
            approval = request.POST[Student1]
            s = Student.objects.get(webmail=student1)
            s.library_approval = approval


'''
def index(request):
    if not request.user.is_authenticated():
        return render(request, 'main/login.html')
    else:
        students = Student.objects.filter(user=request.user)
        faculty_results = Faculty.objects.all()
        query = request.GET.get("q")
        if query:
            students = students.filter(
                Q(department__icontains=query) |
                Q(hostel__icontains=query)
            ).distinct()
            faculty_results= faculty_results.filter(
                Q(department__icontains=query)
            ).distinct()
            return render(request, 'main/index.html', {
                'students': students,
                'facultys': faculty_results,
            })
        else:
            return render(request, 'main/index.html', {'students': students})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'main/login.html', context)

'''
# Create your views here.
