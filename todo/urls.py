from django.urls import path
from .views import TodoAddView, TodoDeleteView, TodoUpdateView, AllTodoGetView, TodoDetailView


urlpatterns = [
    path("todo-add", TodoAddView.as_view()),
    path("todo-delete/<int:id>", TodoDeleteView.as_view()),
    path("todo-update/<int:id>", TodoUpdateView.as_view()),
    path("all-todo-get", AllTodoGetView.as_view()),
    path("todo-detail/<int:id>", TodoDetailView.as_view()),
]
