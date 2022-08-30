from django.urls import path
from .views import *
urlpatterns = [
     path('',home,name='home'),
     path('detail/<str:slug>',DetailToDo,name='todo-detail'),
     path('create/',ToDoCreate,name='todo-create'),
     path('update/<str:slug>',ToDoUpdate,name='todo-update'),
     path('delete/<str:slug>',ToDoDelete,name='todo-delete'),
     
]
