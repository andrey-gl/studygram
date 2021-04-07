from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, StatusTask, User, Course, StatusCourse
from .forms import TaskCreateForm, CourseCreateForm

# TODO: Добавить удаление
# TODO: Добавить поиск в фильтрах студенты/преподаватели
"""Функции ниже относятся к странице "Задания" """


def tasks_list(request):
    status_query = request.GET.get('status')
    teacher_query = request.GET.get('teacher')
    student_query = request.GET.get('student')
    statuses = StatusTask.objects.all()
    teachers = User.objects.filter(Type=1)
    students = User.objects.filter(Type=2)
    if teacher_query is not None:
        tasks = Task.objects.filter(Teacher=teacher_query)
    elif status_query is not None:
        tasks = Task.objects.filter(status_id=int(status_query))
    elif student_query is not None:
        tasks = Task.objects.filter(Student=student_query)
    else:
        tasks = Task.objects.all()
    context = {
        'tasks': tasks,
        'statuses': statuses,
        'teachers': teachers,
        'students': students
    }
    return render(request, template_name='courses/tasks.html', context=context)


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    statuses = StatusTask.objects.all()
    context = {
        'task': task,
        'statuses': statuses
    }
    return render(request, template_name='courses/task.html', context=context)


def CreateTask(request):
    if request.method == "POST":
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            status = form.cleaned_data['status']
            teacher = form.cleaned_data['Teacher']
            student = form.cleaned_data['Student']
            start_date = form.cleaned_data['Start_date']
            deadline = form.cleaned_data['Deadline']
            task = Task.objects.create(name=name, description=description, status=status, Start_date=start_date,
                                       Deadline=deadline)
            task.Teacher.add(*teacher)
            task.Student.add(*student)
            return redirect('/')
    else:
        form = TaskCreateForm()
        context = {
            'form': form
        }
    return render(request, 'courses/create_task.html', context=context)


"""Функции ниже относятся к странице "Курсы" """


def courses_list(request):
    status_query = request.GET.get('status')
    teacher_query = request.GET.get('teacher')
    student_query = request.GET.get('student')
    statuses = StatusCourse.objects.all()
    teachers = User.objects.filter(Type=1)
    students = User.objects.filter(Type=2)
    if teacher_query is not None:
        courses = Course.objects.filter(Teacher=teacher_query)
    elif status_query is not None:
        courses = Course.objects.filter(status_id=int(status_query))
    elif student_query is not None:
        courses = Course.objects.filter(Student=student_query)
    else:
        courses = Course.objects.all()
    context = {
        'courses': courses,
        'statuses': statuses,
        'teachers': teachers,
        'students': students
    }
    return render(request, template_name='courses/courses.html', context=context)

# TODO: Добавить фильтры на курсы


def create_course(request):
    if request.method == "POST":
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            teacher = form.cleaned_data['Teacher']
            student = form.cleaned_data['Student']
            course = Course.objects.create(name=name)
            course.teachers.add(*teacher)
            course.students.add(*student)
            return redirect('/courses')
    else:
        form = CourseCreateForm()

    context = {
        'form': form
    }
    return render(request, template_name='courses/create_course.html', context=context)