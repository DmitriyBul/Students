from django.contrib import admin

# Register your models here.
from .models import Group, Student, Info_About_Models


class StudentInline(admin.TabularInline):
    model = Student


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [
        StudentInline,
    ]
    list_display = ['title', 'group_leader']
    list_filter = ['title', 'group_leader']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['fio', 'birth_date', 'student_ticket', 'group']
    list_filter = ['fio', 'birth_date', 'student_ticket', 'group']


@admin.register(Info_About_Models)
class Info_About_ModelsAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'model_editing', 'model_create', 'model_delete']

