from django.contrib import admin
from main.models import *

class Stud_Faculty_StatusInline(admin.TabularInline):
	model = Stud_Faculty_Status
	extra = 1

class Stud_Lab_StatusInline(admin.TabularInline):
    model = Stud_Lab_Status
    extra = 1


class FacultyAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = (Stud_Faculty_StatusInline,)
    list_display = ('name','department',)

class LabAdmin(admin.ModelAdmin):
    search_fields = ['name','webmail',]
    inlines = (Stud_Lab_StatusInline,)
    list_display = ('name','webmail',)

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['roll_no']
    list_display = ('name',)
    inlines = (Stud_Faculty_StatusInline,Stud_Lab_StatusInline,)
    filter_horizontal = ('faculty_approval', 'lab_approval',)

class CCAdmin(admin.ModelAdmin):
    #search_fields = ['name']
    list_display = ('name','webmail',)

class LibraryAdmin(admin.ModelAdmin):
    #search_fields = ['name',]
    list_display = ('name','webmail',)

class AssiRegAdmin(admin.ModelAdmin):
    #search_fields = ['name',]
    list_display = ('name','webmail',)

class GymkhanaAdmin(admin.ModelAdmin):
    #search_fields = ['name']
    list_display = ('name','webmail',)

class CaretakerAdmin(admin.ModelAdmin):
    search_fields = ['name','hostel','webmail',]
    list_display = ('name','hostel','webmail',)

class WardenAdmin(admin.ModelAdmin):
    search_fields = ['name','hostel','webmail',]
    list_display = ('name','hostel','webmail',)

class HODAdmin(admin.ModelAdmin):
    search_fields = ['name','department','webmail',]
    list_display = ('name','department','webmail',)

class AccountAdmin(admin.ModelAdmin):
    #search_fields = ['name']
    list_display = ('name','webmail',)

class OnlineCCAdmin(admin.ModelAdmin):
    #search_fields = ['name']
    list_display = ('name','webmail',)

class SubmitThesisAdmin(admin.ModelAdmin):
    #search_fields = ['name']
    list_display = ('name','webmail',)

admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Lab, LabAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(HOD, HODAdmin)
admin.site.register(CC, CCAdmin)
admin.site.register(Library, LibraryAdmin)
admin.site.register(Gymkhana, GymkhanaAdmin)
admin.site.register(Assistant_registrar, AssiRegAdmin)
admin.site.register(Caretaker, CaretakerAdmin)
admin.site.register(Warden, WardenAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(OnlineCC, OnlineCCAdmin)
admin.site.register(SubmitThesis, SubmitThesisAdmin)