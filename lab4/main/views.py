from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo, Task

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'task_list.html', {'todos': todos})

def completed_todo_list(request, todo_id):
    todo = [Todo.objects.get(id = todo_id)]
    print(todo)
    tasks = Task.objects.filter(todo = todo[0], is_done = True)
    return render(request, 'task_list.html', {
        'todos': todo,
        'tasks': tasks,
        'show_completed': True,
    })