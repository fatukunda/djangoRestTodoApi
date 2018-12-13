from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Todo

def get_todos(request):
    MAX_OBJECTS = 20
    todos = Todo.objects.all()[: MAX_OBJECTS]
    data = {
        "results": list(todos.values('todo', 'completed', 'created_by'))
    }
    return JsonResponse(data)


def get_single_todo(request, id):
    todo = get_object_or_404(Todo, id = id)
    data = {
        "results": {
            "todo": todo.todo,
            "completed": todo.completed,
            # "created_by": todo.created_by
        }
    }
    return JsonResponse(data)
