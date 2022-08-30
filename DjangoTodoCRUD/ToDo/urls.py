from django.urls import path,include
from .views import *
urlpatterns = [
     
     path('',ToDoListView.as_view(),name='todo-list'),
     path('detail/<int:pk>',ToDoDetailView.as_view(),name='todo-detail'),
     path('create/',ToDoCreateView.as_view(),name='todo-create'),
      path('update/<int:pk>', ToDoUpdateView.as_view(), name='todo-update'),
      path('delete/<int:pk>', ToDoDeleteView.as_view(), name='todo-delete'),
]