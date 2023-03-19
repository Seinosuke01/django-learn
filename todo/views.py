from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Todo, Tag
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


class TodoAddView(APIView):
    def post(self, request):
        Todo.objects.create(
            title=request.data["title"],
            description=request.data["description"],
            completed=request.data["completed"],
            priority=request.data["priority"],
            dueDate=request.data["dueDate"],
        )
        return Response(status=201)


class TodoDeleteView(APIView):
    def delete(self, request, id):
        todo = Todo.objects.get(id=id)  # 本当は例外処理を書く必要があります
        todo.delete()
        return Response(status=204)


class TodoUpdateView(APIView):
    def put(self, request, id):
        todo = Todo.objects.get(id=id)
        todo.title = request.data["title"]
        todo.description = request.data["description"]
        todo.completed = request.data["completed"]
        todo.priority = request.data["priority"]
        todo.dueDate = request.data["dueDate"]
        todo.save()
        return Response(status=200)


class AllTodoGetView(APIView):
    def get(self, request):
        tasks = Todo.objects.all()
        data = {"tasks": list(tasks.values())}
        return JsonResponse(data)
    
class TodoDetailView(APIView):
    def get(self, request, id):
        todo = Todo.objects.get(id=id)
        data = {
                "title": todo.title, 
                "description": todo.description, 
                "completed": todo.completed, 
                "priority": todo.priority, 
                "dueDate": todo.dueDate
                }
        return JsonResponse(data)
