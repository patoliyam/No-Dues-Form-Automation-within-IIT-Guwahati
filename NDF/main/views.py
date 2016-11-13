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
                # print type(Student.webmail)
                username=str(username)
                if role == "Student":
                    return render((stud_profile), username)
                    #url = reverse('stud_profile', kwargs={'username': username})
                    #return HttpResponseRedirect(url)
                return render(request, 'main/login.html', {'error_message': 'Unsuccessful Login'})
        else:
            return render(request, 'main/login.html', {'error_message': 'Invalid login'})
    return render(request, 'main/login.html',{'error_message': 'Valid login it was!'})

def stud_profile(request, username):
    username=request.POST['username']
    stud = Student.objects.filter(webmail=username)

    return render(request, 'main/stud.html',caretaker_approval = Student.objects.filter(webmail=username).values('caretaker_approval')
    #print caretaker_approval
    warden_approval = Student.objects.filter(webmail=username).values('warden_approval')
    gymkhana_approval = Student.objects.filter(webmail=username).values('gymkhana_approval')
    library_approval = Student.objects.filter(webmail=username).values('library_approval')
    CC_approval = Student.objects.filter(webmail=username).values('CC_approval')
    assistant_registrar_approval = Student.objects.filter(webmail=username).values('assistant_registrar_approval')
    HOD_approval = Student.objects.filter(webmail=username).values('HOD_approval')
    account_approval = Student.objects.filter(webmail=username).values('account_approval')
    submit_thesis = Student.objects.filter(webmail=username).values('submit_thesis')
    online_cc_approval = Student.objects.filter(webmail=username).values('online_cc_approval')
    #department = Student.objects.filter(webmail=username).values('department')
    name = Student.objects.filter(webmail=username).values('name')
    dept_status = stud[0].dept_status()
    lab_status = stud[0].lab_status()
                  {'error_message': 'valid login1', 'lab_status': str(lab_status), 'dept_status': str(dept_status),
                   'name': str(name[0]['name']), 'online_cc_approval': str(online_cc_approval[0]['online_cc_approval']),
                   'submit_thesis': str(submit_thesis[0]['submit_thesis']),
                   'caretaker_approval': str(caretaker_approval[0]['caretaker_approval']),
                   'warden_approval': str(warden_approval[0]['warden_approval']),
                   'gymkhana_approval': str(gymkhana_approval[0]['gymkhana_approval']),
                   'library_approval': str(library_approval[0]['library_approval']),
                   'CC_approval': str(CC_approval[0]['CC_approval']),
                   'assistant_registrar_approval': str(assistant_registrar_approval[0]['assistant_registrar_approval']),
                   'HOD_approval': str(HOD_approval[0]['HOD_approval']),
                   account_approval: str(account_approval[0]['account_approval'])})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'main/login.html', context)

def stud_full_dept(request):
    #thisstud = Student.objects.get(pk=album_id)
    #album.delete()
    #albums = Album.objects.filter(user=request.user)

    return render(request, 'main/stud_full_dept.html', {'error_message': 'logged in successfully'})
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
