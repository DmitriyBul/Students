from django.contrib import admin

# Register your models here.
from .models import Group, Student


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'group_leader']
    list_filter = ['title', 'group_leader']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['fio', 'birth_date', 'student_ticket', 'group']
    list_filter = ['fio', 'birth_date', 'student_ticket', 'group']