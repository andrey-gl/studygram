from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from enum import auto
import datetime


class user_type(models.Choices):
    Teacher = auto()
    Student = auto()
    Admin = auto()


class UserStatus(models.Choices):
    Active = auto()
    Deleted = auto()

    def __str__(self):
        return self.name


class StatusCourse(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class StatusTask(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class GroupModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(AbstractUser):
    Otchestvo = models.CharField(max_length=150, blank=True, verbose_name='Отчество')
    Group = models.ManyToManyField(GroupModel, verbose_name='Группа', blank=True)
    Photo = models.ImageField(verbose_name='Фото', blank=True)
    Type = models.SmallIntegerField(choices=user_type.choices, default=2)
    Status = models.SmallIntegerField(choices=UserStatus.choices, default=1)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Task(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    status = models.ForeignKey(StatusTask, on_delete=models.CASCADE, default=2)
    Teacher = models.ManyToManyField(User, related_name='Teachers')
    Student = models.ManyToManyField(User, related_name='Students')
    Start_date = models.DateField(default=datetime.date.today)
    Deadline = models.DateField(default=datetime.date.today)

    def get_absolute_url(self):
        return reverse('task', kwargs={'pk': self.pk,
                                       'teachers': self.Teacher.all().values_list('Teachers', flat=True),
                                       'students': self.Student.all().values_list('Students', flat=True)})

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=150)
    teachers = models.ManyToManyField(User, related_name='CourseTeachers')
    students = models.ManyToManyField(User, related_name='CourseStudents')
    status = models.ForeignKey(StatusCourse, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('courses', kwargs={'pk': self.pk,
                                         'teachers': self.teachers.all().values_list('Teachers', flat=True),
                                         'students': self.students.all().values_list('Students', flat=True)})
