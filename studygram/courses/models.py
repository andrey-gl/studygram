from django.db import models
from django.urls import reverse


class Status(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('task', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
