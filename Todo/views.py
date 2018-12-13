from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer

class TodoList(APIView):
    def get(self, request):
        todos = Todo.objects.all()[:20]
        data = TodoSerializer(todos, many=True).data
        return Response(data)

class TodoDetails(APIView):
    
    def get(self, request, id):
        todo = get_object_or_404(Todo, id = id)
        data = TodoSerializer(todo).data
        return Response(data)

