from django.shortcuts import render, get_object_or_404
from .models import Task, Status


def tasks_list(request):
    query = request.GET.get('status')
    statuses = Status.objects.all()
    if query is not None:
        tasks = Task.objects.filter(status_id=int(query))
    else:
        tasks = Task.objects.all()
    context = {
        'tasks': tasks,
        'statuses': statuses
    }
    return render(request, template_name='courses/tasks.html', context=context)


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    statuses = Status.objects.all()
    context = {
        'task': task,
        'statuses': statuses
    }
    return render(request, template_name='courses/task.html', context=context)
