from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
import datetime


class UserType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class UserStatus(models.Model):
    name = models.CharField(max_length=150)

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


class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(AbstractUser):
    Otchestvo = models.CharField(max_length=150, blank=True, verbose_name='Отчество')
    Group = models.ManyToManyField(Group, verbose_name='Группа', blank=True)
    Photo = models.ImageField(verbose_name='Фото', blank=True)
    Type = models.ForeignKey(UserType, on_delete=models.CASCADE, related_name='type', default=1)
    Status = models.ForeignKey(UserStatus, on_delete=models.CASCADE, related_name='status', default=2)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Course(models.Model):
    name = models.CharField(max_length=150)
    teachers = models.ManyToManyField(User, related_name='CourseTeachers')
    students = models.ManyToManyField(User, related_name='CourseStudents')
    status = models.ForeignKey(StatusCourse, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('course', kwargs={'pk': self.pk})


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
