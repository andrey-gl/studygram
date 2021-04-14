from django import forms
from .models import User, Task, Course


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Teacher'].queryset = User.objects.filter(Type=1)
        self.fields['Student'].queryset = User.objects.filter(Type=2)


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teachers'].queryset = User.objects.filter(Type=1)
        self.fields['students'].queryset = User.objects.filter(Type=2)
