from django.db import models
from django.utils import timezone
# Create your models here.

class Todo(models.Model):
     title = models.CharField( max_length=50,unique=True)
     descriptions = models.TextField()
     date_created = models.DateTimeField(default=timezone.now)
     
     class Meta:
          ordering = ['-date_created']
          
     def __str__(self):
          return self.title

    


