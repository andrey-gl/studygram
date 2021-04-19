from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, StatusTask, Course, StatusCourse
from users.models import User
from .forms import TaskCreateForm, CourseCreateForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.db.models import Q
from django.core.serializers import serialize
from .utils import get_user_list
"""Функции ниже относятся к странице "Задания" """


class TasksList(ListView):
    model = Task
    template_name = 'courses/tasks.html'
    context_object_name = 'tasks'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = User.objects.filter(Type=1)
        context['students'] = User.objects.filter(Type=2)
        context['statuses'] = StatusTask.objects.all()
        return context

    def get_queryset(self):
        status_query = self.request.GET.get('status')
        teacher_query = self.request.GET.get('teacher')
        student_query = self.request.GET.get('student')
        if teacher_query is not None:
            queryset = Task.objects.filter(Teacher=teacher_query)
        elif status_query is not None:
            queryset = Task.objects.filter(status_id=int(status_query))
        elif student_query is not None:
            queryset = Task.objects.filter(Student=student_query)
        else:
            queryset = Task.objects.all()
        return queryset


class TaskView(DetailView):
    model = Task
    template_name = 'courses/task.html'
    context_object_name = 'task'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = StatusTask.objects.all()
        return context


class CreateTask(CreateView):
    form_class = TaskCreateForm
    template_name = 'courses/create_task.html'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        instance = form.save()
        teachers = form.cleaned_data['Teacher']
        students = form.cleaned_data['Student']
        instance.Teacher.add(*teachers)
        instance.Student.add(*students)
        instance.save()
        return super().form_valid(form)


"""Функции ниже относятся к странице "Курсы" """


class CoursesList(ListView):
    model = Course
    template_name = 'courses/courses.html'
    context_object_name = 'courses'
    success_url = reverse_lazy('courses')
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = get_user_list(User.objects.filter(Type=1))
        context['students'] = get_user_list(User.objects.filter(Type=2))
        context['statuses'] = StatusCourse.objects.all()
        return context

    def get_queryset(self):
        search_query = self.request.GET.get('search')
        status_query = self.request.GET.get('status')
        teacher_query = self.request.GET.get('teacher')
        student_query = self.request.GET.get('student')
        if search_query is not None:
            queryset = self.model.objects.filter(Q(name__icontains=search_query) |
                                                 Q(teachers__first_name__icontains=search_query) |
                                                 Q(students__first_name__icontains=search_query) |
                                                 Q(status__name__icontains=search_query)).distinct()
        elif teacher_query is not None:
            queryset = Course.objects.filter(teachers=teacher_query)
        elif status_query is not None:
            queryset = Course.objects.filter(status_id=int(status_query))
        elif student_query is not None:
            queryset = Course.objects.filter(students=student_query)
        else:
            queryset = Course.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        if self.request.is_ajax and self.request.method == "POST":
            courses = self.request.POST.getlist('courses[]')
            pk = self.request.POST.getlist('pk')
            print(self.request.POST.getlist)
            if courses:
                courses = [int(course) for course in courses]
                for course in courses:
                    Course.objects.get(pk=course).delete()
                return HttpResponse(status=200)
            elif pk:
                Course.objects.get(pk=int(pk[0])).delete()
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=400)


class CourseView(DetailView):
    model = Course
    template_name = 'courses/course.html'
    context_object_name = 'courses'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = User.objects.filter(Type=1)
        context['students'] = User.objects.filter(Type=2)
        context['statuses'] = StatusTask.objects.all()
        context['tasks'] = Task.objects.filter(course=self.kwargs['pk'])
        return context


class CreateCourse(CreateView):
    form_class = CourseCreateForm
    success_url = reverse_lazy('courses')
    template_name = 'courses/create_course.html'

    def form_valid(self, form):
        instance = form.save()
        teachers = form.cleaned_data['teachers']
        students = form.cleaned_data['students']
        instance.teachers.add(*teachers)
        instance.students.add(*students)
        return super().form_valid(form)
