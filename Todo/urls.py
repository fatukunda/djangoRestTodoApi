from django.urls import path
from .views import get_todos, get_single_todo

urlpatterns = [
    path('todos/', get_todos, name='todos-list'),
    path('todos/<int:id>/', get_single_todo, name='single-todo')
]