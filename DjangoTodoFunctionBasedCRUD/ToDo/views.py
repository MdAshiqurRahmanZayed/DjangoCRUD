from multiprocessing import context
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse 
from .models import *
from .forms import *
# Create your views here.
#list 
def home(request):
     todolists = ToDo.objects.all().order_by('-date_created')
     context = {
          'todolists':todolists
     }
     return render(request,'ToDoList.html',context)

#detail Todo
def DetailToDo(request,slug):
     todolist = ToDo.objects.get(slug=slug)
     # todolist = ToDo.objects.all().filter(title = str)
     context = {
          'todolist' : todolist
     }
     return render(request,'ToDodetail.html',context)

#Create

def ToDoCreate(request):
     # print(request.POST)
     form = ToDoForm(request.POST or None)
     
     if form.is_valid():
          form.save()
          return redirect('/')
     context ={
          'form' : form
     }
     return render(request,'TodoForm.html',context)

#Update

def ToDoUpdate(request,slug):
     test = ToDo.objects.get(slug=slug)
     form = ToDoForm(request.POST or None,instance=test)
     
     if form.is_valid():
          form.save()
          return redirect('/')
     
     context = {
          'form':form,
          'test':test,
     }
     return render(request,'TodoForm.html',context)
     
     
def ToDoDelete(request,slug):
     object = ToDo.objects.get(slug = slug)
     if request.method =="POST":
          object.delete()
          return redirect("/")
     context = {
          'object' :object
     }
     return render(request,'confirm.html',context)
          