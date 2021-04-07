from django import forms
from .models import StatusTask, User, StatusCourse


class TaskCreateForm(forms.Form):
    name = forms.CharField(max_length=150, label='Название')
    description = forms.CharField(label='Описание', required=False)
    status = forms.ModelChoiceField(queryset=StatusTask.objects.all(), label='Статус')
    Teacher = forms.ModelMultipleChoiceField(queryset=User.objects.filter(Type=1), label='Преподаватель')
    Student = forms.ModelMultipleChoiceField(queryset=User.objects.filter(Type=2), label='Студенты')
    Start_date = forms.DateField(label='Дата начала')
    Deadline = forms.DateField(label='Дата окончания')


class CourseCreateForm(forms.Form):
    name = forms.CharField(max_length=150, label='Название курса')
    Teacher = forms.ModelMultipleChoiceField(queryset=User.objects.filter(Type=1), label='Преподаватель')
    Student = forms.ModelMultipleChoiceField(queryset=User.objects.filter(Type=2), label='Студенты')