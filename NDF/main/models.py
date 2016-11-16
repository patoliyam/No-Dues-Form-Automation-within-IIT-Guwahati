#from __future__ import unicode_literals

from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=250, blank=True)
    webmail = models.CharField(max_length=250, unique=True, blank=True)
    password = models.CharField(max_length=250, blank=True)
    #availability = models.BooleanField(default=True)
    department = models.CharField(max_length=250, blank=True)
    def __str__(self):
        return self.name

class Lab(models.Model):
    name = models.CharField(max_length=250, blank=True)
    webmail = models.CharField(max_length=250, unique=True, blank=True)
    password = models.CharField(max_length=250, blank=True)
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=250, blank=True)
    webmail = models.CharField(max_length=250, unique=True, blank=True)
    password = models.CharField(max_length=250, blank=True)
    roll_no = models.IntegerField(default=0)
    hostel = models.CharField(max_length=250, blank=True)
    department = models.CharField(max_length=250,blank=True)
    faculty_approval = models.ManyToManyField(Faculty, through='Stud_Faculty_Status')
    lab_approval = models.ManyToManyField(Lab, through= 'Stud_Lab_Status')
    caretaker_approval  = models.BooleanField(default=False)
    warden_approval = models.BooleanField(default=False)
    gymkhana_approval = models.BooleanField(default=False)
    HOD_approval = models.BooleanField(default=False)
    assistant_registrar_approval = models.BooleanField(default=False)
    CC_approval = models.BooleanField(default=False)
    library_approval = models.BooleanField(default=False)
    account_approval = models.BooleanField(default=False)
    online_cc_approval = models.BooleanField(default=True)
    submit_thesis = models.BooleanField(default=True)

    def dept_status(self):
        faculty_dept=Faculty.objects.filter(department=self.department)
        dept_status = True
        for fac in faculty_dept:
            status = Stud_Faculty_Status.objects.get(faculty=fac, student=self).faculty_approval
            if status is False:
                dept_status = False
                break
        return dept_status

    def lab_status(self):
        labs=Lab.objects.all()
        lab_status = True
        for lab in labs:
            status = Stud_Lab_Status.objects.get(lab=lab, student=self).lab_approval
            if status is False:
                lab_status = False
                break
        return lab_status

    def __str__(self):
        return self.name

class Stud_Faculty_Status(models.Model):
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    faculty_approval = models.BooleanField(default = False)

    def __str__(self):
        return self.student.name


class Stud_Lab_Status(models.Model):
    lab = models.ForeignKey(Lab,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    lab_approval = models.BooleanField(default=False)
    def __str__(self):
        return self.student.webmail


class Caretaker(models.Model):
    name = models.CharField(max_length=250, blank=True)
    webmail = models.CharField(max_length=250, unique=True, blank=True)
    password = models.CharField(max_length=250, blank=True)
    hostel = models.CharField(max_length=250, blank=True)
    def __str__(self):
        return self.name

class Warden(models.Model):
    name = models.CharField(max_length=250, blank=True)
    webmail = models.CharField(max_length=250, unique=True, blank=True)
    password = models.CharField(max_length=250, blank=True)
    hostel = models.CharField(max_length=250,blank=True)
    def __str__(self):
        return self.name

class Assistant_registrar(models.Model):
    name = models.CharField(max_length=250, default='Assi. Registrar')
    webmail = models.CharField(max_length=250, unique=True, blank=True)
    password = models.CharField(max_length=250,blank=True)
    def __str__(self):
        return self.name

class HOD(models.Model):
    name = models.CharField(max_length=250, blank=True)
    webmail = models.CharField(max_length=250, unique=True, blank=True)
    password = models.CharField(max_length=250,blank=True)
    department = models.CharField(max_length=250,blank=True)
    def __str__(self):
        return self.name

class CC(models.Model):
    name = models.CharField(max_length=250, default='Computer Center')
    webmail = models.CharField(max_length=250, unique=True,blank=True)
    password = models.CharField(max_length=250,blank=True)
    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=250, default='Library')
    webmail = models.CharField(max_length=250, unique=True,blank=True)
    password = models.CharField(max_length=250,blank=True)
    def __str__(self):
        return self.name

class Gymkhana(models.Model):
    name = models.CharField(max_length=250, default='Gymkhana')
    webmail = models.CharField(max_length=250, unique=True,blank=True)
    password = models.CharField(max_length=250,blank=True)
    def __str__(self):
        return self.name

class OnlineCC(models.Model):
    name = models.CharField(max_length=250, default='OnlineCC Manager')
    webmail = models.CharField(max_length=250, unique=True,blank=True)
    password = models.CharField(max_length=250,blank=True)
    def __str__(self):
        return self.name

class SubmitThesis(models.Model):
    name = models.CharField(max_length=250, default='Thesis Manager')
    webmail = models.CharField(max_length=250, unique=True,blank=True)
    password = models.CharField(max_length=250,blank=True)
    def __str__(self):
        return self.name

class Account(models.Model):
    name = models.CharField(max_length=250, default='Account')
    webmail = models.CharField(max_length=250, unique=True,blank=True)
    password = models.CharField(max_length=250,blank=True)
    def __str__(self):
        return self.name