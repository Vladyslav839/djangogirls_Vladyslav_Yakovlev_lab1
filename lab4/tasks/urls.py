from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list_create),
    path('tasks/<int:pk>/done/', views.task_mark_done),
    path('tasks/<int:pk>/', views.task_delete),
]

