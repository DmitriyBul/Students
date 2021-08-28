from django.core.management.base import BaseCommand
from students.models import Group, Student


class Command(BaseCommand):
    help = 'Displays list of groups and students'

    def handle(self, *args, **kwargs):
        groups = list(Group.objects.values_list('title', flat=True))
        for group in groups:
            group_of_student = Group.objects.get(title=group)
            students = list(Student.objects.filter(group=group_of_student.id).values_list('fio', flat=True))
            self.stdout.write("Group: %s" % group_of_student.title)
            self.stdout.write("Students: %s" % students)
