# Generated by Django 3.2.6 on 2021-08-17 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='students.group'),
        ),
    ]
