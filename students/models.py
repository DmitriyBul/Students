from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify


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
