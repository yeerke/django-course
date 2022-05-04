from django.contrib import admin
from .models import Task, Todo, TodoList

admin.site.register(Task)
admin.site.register(Todo)
admin.site.register(TodoList)
