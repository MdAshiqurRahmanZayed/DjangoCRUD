from django.urls import path
from .views import *
urlpatterns = [
     path('',home,name='home'),
     path('detail/<str:str>',DetailToDo,name='todo-detail'),
     path('create/',ToDoCreate,name='todo-create'),
     path('update/<str:str>',ToDoUpdate,name='todo-update'),
     path('delete/<str:str>',ToDoDelete,name='todo-delete'),
     
]
