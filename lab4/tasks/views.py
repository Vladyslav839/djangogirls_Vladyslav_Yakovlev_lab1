from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Task
from .serializers import TaskSerializer


@api_view(['GET', 'POST'])
def task_list_create(request):

    if request.method == 'GET':
        tasks = Task.objects.all().order_by('-created')
        serializer = TaskSerializer(tasks, many=True)
        return Response({'tasks': serializer.data})

    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def task_mark_done(request, pk):

    task = get_object_or_404(Task, pk=pk)


    task.done = True
    task.save()

    serializer = TaskSerializer(task)
    return Response(serializer.data)


@api_view(['DELETE'])
def task_delete(request, pk):

    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
