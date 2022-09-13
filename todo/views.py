from functools import partial
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from todo.models import Todo

from .serializers import TodoSerializer
from .models import Todo

class TodoViews(APIView):
    def get(self, request, id=None):
        if id:
            queryset = Todo.objects.get(id=id)
            todo = TodoSerializer(queryset)
            return Response(todo.data)

        queryset = Todo.objects.all()
        todos = TodoSerializer(queryset, many=True)
        return Response(todos.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({ 'status': 'success', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({ 'status': 'error', 'data': serializer.errors }, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        queryset = Todo.objects.get(id=id)
        todo = TodoSerializer(queryset, data=request.data, partial=True)

        if todo.is_valid():
            todo.save()
            return Response({ 'status': 'success', 'data': todo.data}, status=status.HTTP_200_OK)
        else:
            return Response({ 'status': 'error', 'data': todo.errors }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        queryset = Todo.objects.get(id=id)
        queryset.delete()
        return Response({ 'status': 'success', 'data': 'Todo deleted' })