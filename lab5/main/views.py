from .models import Task, Todo, TodoList
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import CompletedTodoSerializer, TodoSerializer, TodoListSerializer
from rest_framework.permissions import IsAuthenticated
from .forms import UploadFileForm

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def todos(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    else:
        serializer = TodoSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_todos_completed(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    serializer = CompletedTodoSerializer(todo, many=False)

    return Response(serializer.data)

@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def get_todos_completed(request, todo_id):
    instance = Todo.objects.get(id=todo_id)
    serializer = CompletedTodoSerializer(data=request.data, instance=instance)

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data)

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def todo_lists(request):
    if request.method == 'GET':
        todo_lists = TodoList.objects.all()
        serializer = TodoListSerializer(todo_lists, many=True)
        return Response(serializer.data)
    else:
        serializer = TodoListSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

@api_view(['GET', 'PUT'])
# @permission_classes([IsAuthenticated])
def todo_list(request, todo_list_id):
    if request.method == 'GET':
        todo_list = TodoList.objects.get(id=todo_list_id)
        serializer = TodoListSerializer(todo_list, many=False)
        return Response(serializer.data)
    else:
        instance = TodoList.objects.get(id=todo_list_id)
        serializer = TodoListSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def todo_list_todos(request, todo_list_id):
    todo_list = Todo.objects.filter(todo_list=todo_list_id)
    serializer = TodoSerializer(todo_list, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def upload_file(request):    
    form = UploadFileForm(request.POST, request.FILES)
    url = request.data.url
    if form.is_valid():
        handle_uploaded_file(request.FILES['file'], url)
        return Response()

def handle_uploaded_file(file, url):
    with open(url, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)