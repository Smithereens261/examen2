from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class PendingTodos(generics.ListAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(is_completed=False)

class CompletedTodos(generics.ListAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(is_completed=True)

class UserTodos(generics.ListAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Todo.objects.filter(user_id=user_id)

class UserCompletedTodos(generics.ListAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Todo.objects.filter(user_id=user_id, is_completed=True)

class UserPendingTodos(generics.ListAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Todo.objects.filter(user_id=user_id, is_completed=False)