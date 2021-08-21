from django import forms
from students.models import Group, Student


class GroupForm(forms.ModelForm):
    title = forms.CharField(label='Title of group', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter a group title'
    }))
    group_leader = forms.ModelChoiceField(
        label='Group leader', queryset=Student.objects.all(), widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = Group
        fields = 'title', 'group_leader'


class StudentForm(forms.ModelForm):
    fio = forms.CharField(label='Name, Surname', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter a full name and surname'
    }))
    birth_date = forms.DateField(label='Day of birth')
    student_ticket = forms.IntegerField(label="Student's ticket")
    group = forms.ModelChoiceField(
        label='Group', queryset=Group.objects.all(), widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = Student
        fields = '__all__'
