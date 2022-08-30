from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from .models import *
from .forms import TodoForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin



class ToDoListView(ListView):
    model = Todo 
    template_name = 'todo_list.html'

class ToDoDetailView(DetailView):
    model = Todo
    template_name = "todo_detail.html"


class ToDoCreateView(SuccessMessageMixin,CreateView):
    model = Todo
    form_class  = TodoForm
    template_name = "todo_form.html"
    success_url = reverse_lazy('todo-list')
    success_message = "ToDo successfully created!"


class ToDoUpdateView(SuccessMessageMixin,UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = "todo_form.html"
    success_url = reverse_lazy('todo-list')
    success_message = "ToDo successfully Updated!"


class ToDoDeleteView(SuccessMessageMixin,DeleteView):
    model = Todo
    template_name = "todo_confirm_delete.html"
    success_url = reverse_lazy('todo-list')
    success_message = "Product successfully deleted!"


