from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, StatusTask, User, Course, StatusCourse
from .forms import TaskCreateForm, CourseCreateForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse

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
        context['teachers'] = User.objects.filter(Type=1)
        context['students'] = User.objects.filter(Type=2)
        context['statuses'] = StatusCourse.objects.all()
        return context

    def get_queryset(self):
        status_query = self.request.GET.get('status')
        teacher_query = self.request.GET.get('teacher')
        student_query = self.request.GET.get('student')
        if teacher_query is not None:
            queryset = Course.objects.filter(teachers=teacher_query)
        elif status_query is not None:
            queryset = Course.objects.filter(status_id=int(status_query))
        elif student_query is not None:
            queryset = Course.objects.filter(students=student_query)
        else:
            queryset = Course.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        courses = self.request.POST.getlist('course')
        single_course = self.request.POST.getlist('course-li')
        print(self.request.POST.getlist)
        if courses:
            courses = [int(course) for course in courses]
            for course in courses:
                Course.objects.get(pk=course).delete()
            return HttpResponseRedirect(reverse_lazy('courses'))
        elif single_course:
            single_course = [int(course) for course in single_course]
            print(single_course)
            Course.objects.get(pk=single_course[0]).delete()
            return HttpResponseRedirect(reverse_lazy('courses'))
        else:
            return HttpResponse(status=400)


class CourseView(ListView):
    model = Task
    template_name = 'courses/course.html'
    context_object_name = 'tasks'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = User.objects.filter(Type=1)
        context['students'] = User.objects.filter(Type=2)
        context['statuses'] = StatusTask.objects.all()
        context['pk'] = self.kwargs['pk']
        context['course'] = self.model.objects.get(course=self.kwargs['pk']).course
        return context

    def get_queryset(self):
        status_query = self.request.GET.get('status')
        teacher_query = self.request.GET.get('teacher')
        student_query = self.request.GET.get('student')
        if status_query is not None:
            queryset = Task.objects.filter(course=self.kwargs['pk'], status=int(status_query))
        elif teacher_query is not None:
            queryset = Task.objects.filter(course=self.kwargs['pk'], Teacher=teacher_query)
        elif student_query is not None:
            queryset = Task.objects.filter(course=self.kwargs['pk'], Student=student_query)
        else:
            queryset = Task.objects.filter(course=self.kwargs['pk'])
        return queryset


class CreateCourse(CreateView):
    form_class = CourseCreateForm
    success_url = reverse_lazy('courses')
    template_name = 'courses/create_course.html'

    def form_valid(self, form):
        instance = form.save()
        teachers = form.cleaned_data['Teacher']
        students = form.cleaned_data['Student']
        instance.teachers.add(*teachers)
        instance.students.add(*students)
        return super().form_valid(form)
