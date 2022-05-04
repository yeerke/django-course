from turtle import done
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    is_done = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)

    def mark(self):
        if self.is_done:
            return 'Done'
        else:
            return 'Not done'

    def __str__(self):
        return self.name
