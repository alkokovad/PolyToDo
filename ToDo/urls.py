from django.urls import path
from . import views


urlpatterns = [
    path('', views.ToDoView.as_view(), name="todo_page"),
]