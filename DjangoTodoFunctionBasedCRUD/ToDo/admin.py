from django.contrib import admin
from .models import *

class ToDoAdmin(admin.ModelAdmin):
     prepopulated_fields = {"slug": ("title",)} 
     

admin.site.register(ToDo,ToDoAdmin)