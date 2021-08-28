from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_init, post_save, post_delete
from django.dispatch import receiver
from datetime import datetime


class Info_About_Models(models.Model):
    model_name = models.CharField(max_length=255, blank=True)
    model_create = models.CharField(max_length=255, blank=True)
    model_editing = models.CharField(max_length=255, blank=True)
    model_delete = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.model_name


class Group(models.Model):
    title = models.CharField(max_length=20)
    group_leader = models.ForeignKey('Student', null=True, blank=True, related_name='group_leader',
                                     on_delete=models.DO_NOTHING)
    slug = models.SlugField(max_length=20, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Group, self).save(*args, **kwargs)

    class Meta:
        ordering = ('title',)
        verbose_name = 'group'
        verbose_name_plural = 'groups'

    def get_absolute_url(self):
        return reverse('students:group_detail', args=[self.slug])

    def __str__(self):
        return self.title


class Student(models.Model):
    fio = models.CharField(max_length=100)
    birth_date = models.DateField()
    student_ticket = models.IntegerField()
    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('fio', 'group')
        verbose_name = 'student'
        verbose_name_plural = 'students'

    def __str__(self):
        return self.fio

    def get_absolute_url(self):
        return reverse('students:student_detail', args=[self.fio])


'''

@receiver(post_init, sender=Student)  # создание новой записи (модель Students)
def post_init_students(instance, **kwargs):
    i_a_m = Info_About_Models.objects.get_or_create(model_name='Student', model_create=datetime.now())

'''


@receiver(post_save, sender=Student)  # редактирование записи (модель Students)
def post_save_students(instance, **kwargs):
    i_a_m = Info_About_Models.objects.get_or_create(model_name='Student', model_editing=datetime.now())


@receiver(post_delete, sender=Student)  # удаление записи (модель Students)
def post_delete_students(instance, **kwargs):
    i_a_m = Info_About_Models.objects.get_or_create(model_name='Student', model_delete=datetime.now())


'''
@receiver(post_init, sender=Group)  # создание новой записи (модель Groups)
def post_init_groups(instance, **kwargs):
    i_a_m = Info_About_Models.objects.get_or_create(model_name='Group', model_create=datetime.now())
'''


@receiver(post_save, sender=Group)  # редактирование записи (модель Groups)
def post_save_groups(instance, **kwargs):
    i_a_m = Info_About_Models.objects.get_or_create(model_name='Group', model_editing=datetime.now())


@receiver(post_delete, sender=Group)  # удаление записи (модель Groups)
def post_delete_groups(instance, **kwargs):
    i_a_m = Info_About_Models.objects.get_or_create(model_name='Group')
