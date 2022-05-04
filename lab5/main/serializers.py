from dataclasses import fields
from rest_framework import serializers
from .models import Task, Todo, TodoList

class CompletedTaskSerializerList(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(is_completed=True)
        return super(CompletedTaskSerializerList, self).to_representation(data)

class CompletedTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        list_serializer_class = CompletedTaskSerializerList
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TodoSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)
    class Meta():
        model = Todo
        fields = '__all__'

    def create(self, validated_data):
        tasks_data = validated_data.pop('tasks')
        todo = Todo.objects.create(**validated_data)
        for task_data in tasks_data:
            Task.objects.create(todo=todo, **task_data)
        return todo

class CompletedTodoSerializer(serializers.ModelSerializer):
    tasks = CompletedTaskSerializer(many=True)
    class Meta():
        model = Todo
        fields = '__all__'

    def create(self, validated_data):
        tasks_data = validated_data.pop('tasks')
        todo = Todo.objects.create(**validated_data)
        for task_data in tasks_data:
            Task.objects.create(todo=todo, **task_data)
        return todo

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class TodoListSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True)
    class Meta():
        model = TodoList
        fields = '__all__'

    def create(self, validated_data):
        todos_data = validated_data.pop('todos')
        todo_list = TodoList.objects.create(**validated_data)

        for todo_data in todos_data:
            tasks_data = todo_data.pop('tasks')
            todo = Todo.objects.create(todo_list=todo_list, **todo_data)
            for task_data in tasks_data:
                Task.objects.create(todo=todo, **task_data)

        return todo_list

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
