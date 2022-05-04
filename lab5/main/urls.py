import imp
from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todos),
    path('todos/<str:todo_id>/', views.get_todos_completed),
    path('todos/<str:todo_id>/completed', views.get_todos_completed),
    path('todo-lists', views.todo_lists),
    path('todo-lists/<str:todo_list_id>/', views.todo_list),
    path('todo-lists/<str:todo_list_id>/todos/', views.todo_list_todos),
]