from django import forms
from .models import User, Task, Course


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'course', 'description', 'status', 'Start_date', 'Deadline', ]
    Teacher = forms.ModelMultipleChoiceField(queryset=User.objects.filter(Type=1), label='Преподаватель')
    Student = forms.ModelMultipleChoiceField(queryset=User.objects.filter(Type=2), label='Студенты')


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']
    Teacher = forms.ModelMultipleChoiceField(queryset=User.objects.filter(Type=1), label='Преподаватель')
    Student = forms.ModelMultipleChoiceField(queryset=User.objects.filter(Type=2), label='Студенты')
