from rest_framework.decorators import api_view
from rest_framework.response import Response

from todo.models import Todo

from .serializers import TodoSerializer
from .models import Todo

@api_view(['GET'])
def get_todos(request):
    queryset = Todo.objects.all()
    todos = TodoSerializer(queryset)
    return Response(todos.data)