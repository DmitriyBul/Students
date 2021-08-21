from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View
from django.db.models import Count

from students.forms import GroupForm, StudentForm
from students.models import Group, Student


class GroupListView(ListView):
    def get(self, request, ordering='AZ', *args, **kwargs):
        group_list = Group.objects.all()
        group_list = Group.objects.annotate(nstud=Count('student'))
        template_name = 'group_list.html'
        context = {'group_list': group_list}
        return render(request, template_name, context)


class GroupDetailView(View):
    def get(self, request, ordering='AZ', *args, **kwargs):
        group = Group.objects.get(slug=self.kwargs['slug'])
        students = Student.objects.filter(group=group).order_by('fio')
        template_name = 'group_detail.html'
        context = {'group': group, 'students': students}
        return render(request, template_name, context)


class StudentDetailView(View):
    def get(self, request, ordering='AZ', *args, **kwargs):
        student = Student.objects.get(fio=self.kwargs['fio'])
        template_name = 'student_detail.html'
        context = {'student': student}
        return render(request, template_name, context)


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/create.html'
    success_url = reverse_lazy('students:group_list')


class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/update.html'
    success_url = reverse_lazy('students:group_list')


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    success_url = reverse_lazy('students:group_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/create.html'
    success_url = reverse_lazy('students:group_list')


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/update.html'
    success_url = reverse_lazy('students:group_list')


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('students:group_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
