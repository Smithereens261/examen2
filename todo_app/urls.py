from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.TodoList.as_view(), name='todo-list'),
    path('todos/<int:pk>/', views.TodoDetail.as_view(), name='todo-detail'),
    path('todos/pendiente/', views.PendingTodos.as_view(), name='pending-todos'),
    path('todos/completo/', views.CompletedTodos.as_view(), name='completed-todos'),
    path('todos/user/<int:user_id>/', views.UserTodos.as_view(), name='user-todos'),
    path('todos/user/<int:user_id>/completo/', views.UserCompletedTodos.as_view(), name='user-completed-todos'),
    path('todos/user/<int:user_id>/pendiente/', views.UserPendingTodos.as_view(), name='user-pending-todos'),
]
