from django.db import models
from django.urls import reverse
from users.models import *
import datetime


class StatusCourse(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус курса'
        verbose_name_plural = 'Статусы курсов'
        ordering = ['id']


class StatusTask(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус задания'
        verbose_name_plural = 'Статусы заданий'
        ordering = ['id']


class Course(models.Model):
    name = models.CharField(max_length=150)
    teachers = models.ManyToManyField(User, related_name='CourseTeachers')
    students = models.ManyToManyField(User, related_name='CourseStudents')
    status = models.ForeignKey(StatusCourse, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('course', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['id']


class Task(models.Model):
    name = models.CharField(max_length=150)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.ForeignKey(StatusTask, on_delete=models.CASCADE, default=2)
    Teacher = models.ManyToManyField(User, related_name='Teachers')
    Student = models.ManyToManyField(User, related_name='Students')
    Start_date = models.DateField(default=datetime.date.today)
    Deadline = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ['id']
