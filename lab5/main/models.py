from django.db import models
from django.contrib.auth.models import User

class TodoList(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Todo(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=100)
    todo_list = models.ForeignKey(TodoList, related_name='todos', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, related_name='tasks', on_delete=models.CASCADE)

    def mark(self):
        if self.is_done:
            return 'Completed'
        else:
            return 'Not completed'

    def __str__(self):
        return self.name

class File(models.Model):
    url = models.CharField(max_length=100)
    todo_list = models.ForeignKey(Todo, related_name='todo', on_delete=models.CASCADE)

