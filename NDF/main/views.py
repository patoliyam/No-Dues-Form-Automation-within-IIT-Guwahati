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
                    return redirect('/stud_profile')
                elif role == "Faculty":
                    return redirect('/faculty_profile')
                elif role == "Lab":
                    return redirect('/lab_profile')
                elif role == "Caretaker":
                    return redirect('/caretaker_profile')
                elif role == "Warden":
                    return redirect('/warden_profile')
                elif role == "Gymkhana":
                    return redirect('/gymkhana_profile')
                elif role == "OnlineCC":
                    return redirect('/onlinecc_profile')
                elif role == "CC":
                    return redirect('/cc_profile')
                elif role == "Thesis Manager":
                    return redirect('/thesis_manager_profile')
                elif role == "Library":
                    return redirect('/library_profile')
                elif role == "Assistant Registrar":
                    return redirect('/assireg_profile')
                elif role == "HOD":
                    return redirect('/hod_profile')
                elif role == "Account":
                    return redirect('/account_profile')
                elif role == "Admin":
                    return redirect('/admin')
                else:
                    return render(request, 'main/login.html', {'error_message': 'Unsuccessful Login'})
            else:
                return render(request, 'main/login.html', {'error_message': 'Session Expired'})
        else:
            return render(request, 'main/login.html', {'error_message': 'Credentials Invalid'})
    return render(request, 'main/login.html',{'error_message': ''})

def stud_profile(request):
    username=request.user.username
    try:
        student = Student.objects.get(webmail=username)
    except Student.DoesNotExist:
        student = None
    if student is None:
        return render(request, 'main/login.html', {'error_message': 'Role mismatch'})
    student = Student.objects.get(webmail=username)
    return render(request, 'main/stud.html', {'error_message': 'valid login', 'student': student})

def rules(request):
    username=request.user.username
    try:
        student = Student.objects.get(webmail=username)
    except Student.DoesNotExist:
        student = None
    return render(request,'main/rules.html', {'student':student})

def contact(request):
    username = request.user.username
    try:
        student = Student.objects.get(webmail=username)
    except Student.DoesNotExist:
        student = None
    return render(request, 'main/contact.html', {'student': student})

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
    student = Student.objects.get(webmail=username)
    labs = Lab.objects.all()
    stud_lab_status = Stud_Lab_Status.objects.filter(student=student)
    return render(request, 'main/stud_full_lab.html', {'error_message': 'valid login', 'student': student, 'labs' : labs, 'Stud_Lab_Status':stud_lab_status})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    return render(request, 'main/login.html', {"form": form})

def faculty_profile(request):
    if request.method == "GET":
        username = request.user.username
        try:
            fac = Faculty.objects.get(webmail=username)
        except Faculty.DoesNotExist:
            fac = None
        if fac is None:
            return render(request, 'main/login.html', {'error_message': 'Role mismatch'})
        #fac = Faculty.objects.get(webmail=username)
        dept = fac.department
        students = Student.objects.filter(department=dept)
        stud_fac_status = Stud_Faculty_Status.objects.filter(faculty=fac)
        return render(request, 'main/faculty.html',
                      {'error_message': 'valid login', 'students': students, 'faculty': fac, 'dept': dept,
                       'Stud_Faculty_Status': stud_fac_status})
    elif request.method=="POST":
        username = request.user.username
        fac = Faculty.objects.get(webmail=username)
        dept = fac.department
        students = Student.objects.filter(department=dept)
        stud_fac_status = Stud_Faculty_Status.objects.filter(faculty=fac)
        for stud in students:
            for i in stud_fac_status :
                if i.student.webmail == stud.webmail:
                    remarks = request.POST[str(stud.roll_no)]
                    print type(remarks)
                    print remarks
                    if request.POST.get(stud.webmail,"") == 'on':
                        x=Stud_Faculty_Status.objects.get(student=stud, faculty=fac)
                        x.faculty_approval=True
                        x.faculty_remarks=remarks
                        x.save()
                        #stud.save()
                        #print Stud_Faculty_Status.objects.get(student=stud, faculty=fac).faculty_approval
                    else :
                        x = Stud_Faculty_Status.objects.get(student=stud, faculty=fac)
                        print x
                        x.faculty_approval=False
                        stud.HOD_approval=False
                        stud.account_approval=False
                        x.faculty_remarks = remarks
                        stud.save()
                        x.save()
                        #print Stud_Faculty_Status.objects.get(student=stud, faculty=fac).faculty_approval
        return redirect('/faculty_profile')

def lab_profile(request):
    if request.method == "GET":
        username = request.user.username
        try:
            lab = Lab.objects.get(webmail=username)
        except Lab.DoesNotExist:
            lab = None
        if lab is None:
            return render(request, 'main/login.html', {'error_message': 'Role mismatch'})
        #lab = Lab.objects.get(webmail=username)
        students = Student.objects.all()
        stud_lab_status = Stud_Lab_Status.objects.filter(lab=lab)
        return render(request, 'main/lab.html',
                      {'error_message': 'valid login', 'students': students, 'lab': lab, 'Stud_Lab_Status': stud_lab_status})
    elif request.method=="POST":
        username = request.user.username
        lab = Lab.objects.get(webmail=username)
        students = Student.objects.all()
        stud_lab_status = Stud_Lab_Status.objects.filter(lab=lab)
        for stud in students:
            for i in stud_lab_status :
                if i.student.webmail == stud.webmail:
                    if request.POST.get(stud.webmail,"") == 'on':
                        x=Stud_Lab_Status.objects.get(student=stud, lab=lab)
                        x.lab_approval=True
                        x.save()
                        #stud.save()
                        #print Stud_Faculty_Status.objects.get(student=stud, faculty=fac).faculty_approval
                    else :
                        x = Stud_Lab_Status.objects.get(student=stud, lab=lab)
                        print x.student
                        x.lab_approval=False
                        stud.HOD_approval=False
                        stud.account_approval=False
                        stud.save()
                        x.save()

                        #print Stud_Faculty_Status.objects.get(student=stud, faculty=fac).faculty_approval
        return redirect('/lab_profile')

def caretaker_profile(request):
    if request.method == "GET":
        username = request.user.username
        try:
            caretaker = Caretaker.objects.get(webmail=username)
        except Caretaker.DoesNotExist:
            caretaker = None
        if caretaker is None:
            return render(request, 'main/login.html', {'error_message': 'Role mismatch'})
        #caretaker = Caretaker.objects.get(webmail=username)
        hostel = caretaker.hostel
        students = Student.objects.filter(hostel=hostel)
        return render(request, 'main/caretaker.html',
                      {'error_message': 'valid login', 'students': students, 'caretaker': caretaker, 'hostel': hostel})
    elif request.method=="POST":
        username = request.user.username
        caretaker = Caretaker.objects.get(webmail=username)
        hostel = caretaker.hostel
        students = Student.objects.filter(hostel=hostel)
        for stud in students:
            if request.POST.get(stud.webmail,"") == 'on':
                stud.caretaker_approval=True
                stud.save()
            else :
                stud.caretaker_approval = False
                stud.warden_approval=False
                stud.assistant_registrar_approval=False
                stud.HOD_approval=False
                stud.account_approval=False
                stud.save()
        return redirect('/caretaker_profile')

def warden_profile(request):
    if request.method == "GET":
        username = request.user.username
        try:
            warden = Warden.objects.get(webmail=username)
        except Warden.DoesNotExist:
            warden = None
        if warden is None:
            return render(request, 'main/login.html', {'error_message': 'Role mismatch'})
        #warden = Warden.objects.get(webmail=username)
        hostel = warden.hostel
        students = Student.objects.filter(hostel=hostel, caretaker_approval=True)
        return render(request, 'main/warden.html',
                      {'error_message': 'valid login', 'students': students, 'warden': warden,
                       'hostel': hostel})
    elif request.method == "POST":
        username = request.user.username
        warden = Warden.objects.get(webmail=username)
        hostel = warden.hostel
        students = Student.objects.filter(hostel=hostel, caretaker_approval=True)
        for stud in students:
            if request.POST.get(stud.webmail, "") == 'on':
                stud.warden_approval = True
                stud.save()
            else:
                stud.warden_approval = False
                stud.assistant_registrar_approval=False
                stud.HOD_approval=False
                stud.account_approval=False
                stud.save()
        return redirect('/warden_profile')

def gymkhana_profile(request):
    if request.method == "GET":
        username = request.user.username
        try:
            gymnkhana = Gymkhana.objects.get(webmail=username)
        except Gymkhana.DoesNotExist:
            gymnkhana = None
        if gymnkhana is None:
            return render(request, 'main/login.html', {'error_message': 'Role mismatch'})
        #gymnkhana = Gymkhana.objects.get(webmail=username)
        students = Student.objects.all()
        return render(request, 'main/gymkhana.html',
                      {'error_message': 'valid login', 'students': students, 'gymkhana': gymnkhana})
    elif request.method == "POST":
        students = Student.objects.all()
        for stud in students:
            if request.POST.get(stud.webmail, "") == 'on':
                stud.gymkhana_approval = True
                stud.save()
            else:
                stud.gymkhana_approval = False
                stud.assistant_registrar_approval=False
                stud.HOD_approval=False
                stud.account_approval=False
                stud.save()
            return redirect('/gymkhana_profile')

def onlinecc_profile(request):
    if request.method == "GET":
        username = request.user.username
        try:
            onlinecc = OnlineCC.objects.get(webmail=username)
        except OnlineCC.DoesNotExist:
            onlinecc = None
        if onlinecc is None:
            return render(request, 'main/login.html', {'error_message': 'Role mismatch'})
        #onlinecc = OnlineCC.objects.get(webmail=username)
        students = Student.objects.all()
        #print students
        return render(request, 'main/onlinecc.html',
                      {'error_message': 'valid login', 'students': students, 'onlinecc': onlinecc})
    elif request.method == "POST":
        students = Student.objects.all()
        for stud in students:
            if request.POST.get(stud.webmail, "") == 'on':
                stud.online_cc_approval = True
                stud.save()
            else:
                stud.online_cc_approval = False
                stud.CC_approval=False
                stud.HOD_approval=False
                stud.account_approval=False
                stud.save()
        return redirect('/onlinecc_profile')

def cc_profile(request):
    if request.method == "GET":
        username = request.user.username
        try:
            cc = CC.objects.get(webmail=username)
        except CC.DoesNotExist:
            cc = None
        if cc is None:
            return render(request, 'main/login.html', {'error_message': 'Role mismatch'})
        #cc = CC.objects.get(webmail=username)
        students = Student.objects.filter(online_cc_approval=True)
        print students
        return render(request, 'main/cc.html',
                      {'error_message': 'valid login', 'students': students, 'cc': cc})
    elif request.method == "POST":
        students = Student.objects.filter(online_cc_approval=True)
        for stud in students:
            if request.POST.get(stud.webmail, "") == 'on':
                stud.CC_approval = True
                stud.save()
            else:
                stud.CC_approval = False
                stud.HOD_approval=False
                stud.account_approval=False
                stud.save()
        return redirect('/cc_profile')

def thesis_manager_profile(request):
    if request.method == "GET":
        username = request.user.username
        try:
            thesis_manager = SubmitThesis.objects.get(webmail=username)
        except SubmitThesis.DoesNotExist:
            thesis_manager = None
        if thesis_manager is None:
            return render(request, 'main/login.html', {'error_message': 'Role mismatch'})
        students = Student.objects.all()
        return render(request, 'main/thesis_manager.html',
                      {'error_message': 'valid login', 'students': students, 'thesis_manager':thesis_manager})
    elif request.method == "POST":
        students = Student.objects.all()
        for stud in students:
            if request.POST.get(stud.webmail, "") == 'on':
                stud.submit_thesis = True
                stud.save()
            else:
                stud.submit_thesis = False
                stud.library_approval=False
                stud.HOD_approval=False
                stud.account_approval=False
                stud.save()
        return redirect('/thesis_manager_profile')

def library_profile(request):
    if request.method == "GET":
        username = request.user.username
        try:
            library = Library.objects.get(webmail=username)
        except Library.DoesNotExist:
            library = None
        if library is None:
            return render(request, 'main/login.html', {'error_message': 'Role mismatch'})
        #library = Library.objects.get(webmail=username)
        students = Student.objects.filter(submit_thesis=True)
        return render(request, 'main/library.html',
                      {'error_message': 'valid login', 'students': students, 'library': library})
    elif request.method == "POST":
        students = Student.objects.filter(submit_thesis=True)
        for stud in students:
            if request.POST.get(stud.webmail, "") == 'on':
                stud.library_approval = True
                stud.save()
            else:
                stud.library_approval = False
                stud.HOD_approval=False
                stud.account_approval=False
                stud.save()
        return redirect('/library_profile')

def assireg_profile(request):
    if request.method == "GET":
        username = request.user.username
        try:
            assistant_registrar = Assistant_registrar.objects.get(webmail=username)
        except Assistant_registrar.DoesNotExist:
            assistant_registrar = None
        if assistant_registrar is None:
            return render(request, 'main/login.html', {'error_message': 'Role mismatch'})
        #assistant_registrar= Assistant_registrar.objects.get(webmail=username)
        students = Student.objects.filter(caretaker_approval=True,warden_approval=True,gymkhana_approval=True)
        return render(request, 'main/assistant_registrar.html',
                      {'error_message': 'valid login', 'students': students, 'assistant_registrar': assistant_registrar})
    elif request.method == "POST":
        students = Student.objects.filter(caretaker_approval=True, warden_approval=True, gymkhana_approval=True)
        for stud in students:
            if request.POST.get(stud.webmail, "") == 'on':
                stud.assistant_registrar_approval = True
                stud.save()
            else:
                stud.assistant_registrar_approval = False
                stud.HOD_approval=False
                stud.account_approval=False
                stud.save()
        return redirect('/assireg_profile')

def hod_profile(request):
    if request.method == "GET":
        username = request.user.username
        try:
            hod = HOD.objects.get(webmail=username)
        except HOD.DoesNotExist:
            hod = None
        if hod is None:
            return render(request, 'main/login.html', {'error_message': 'Role mismatch'})
        #hod = HOD.objects.get(webmail=username)
        students = Student.objects.filter(department=hod.department, assistant_registrar_approval=True,
                                          library_approval=True, CC_approval=True)
        # print students
        # print 1
                                          #lab_status=True, dept_status=True)
        return render(request, 'main/hod.html',
                      {'error_message': 'valid login', 'students': students,
                       'hod': hod})
    elif request.method == "POST":
        username = request.user.username
        hod = HOD.objects.get(webmail=username)
        students = Student.objects.filter(department=hod.department, assistant_registrar_approval=True,
                                          library_approval=True, CC_approval=True)
        #print students[0].lab_status()

        for stud in students:
            print stud.name
            print (stud.lab_status()is True)
            if stud.lab_status() is True:
                if stud.dept_status() is True:
                    if request.POST.get(stud.webmail, "") == 'on':
                        stud.HOD_approval = True
                        stud.save()
                    else:
                        stud.HOD_approval = False
                        stud.account_approval=False
                        stud.save()
        return redirect('/hod_profile')

def account_profile(request):
    if request.method == "GET":
        username = request.user.username
        try:
            account = Account.objects.get(webmail=username)
        except Account.DoesNotExist:
            account = None
        if account is None:
            return render(request, 'main/login.html', {'error_message': 'Role mismatch'})
        #account = Account.objects.get(webmail=username)
        students = Student.objects.filter(HOD_approval=True)
        print students
        return render(request, 'main/account.html',
                      {'error_message': 'valid login', 'students': students, 'account': account})
    elif request.method == "POST":
        students = Student.objects.filter(HOD_approval=True)
        print students
        for stud in students:
            if request.POST.get(stud.webmail, "") == 'on':
                print stud.name
                stud.account_approval = True
                stud.save()
            else:
                print stud.name
                stud.account_approval = False
                stud.save()
        return redirect('/account_profile')
# Create your views here.
