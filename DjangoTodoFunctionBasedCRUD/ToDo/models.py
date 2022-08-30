from turtle import title
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
class ToDo(models.Model):
     title = models.CharField( max_length=100,unique=True)
     descriptions = models.TextField()
     date_created = models.DateTimeField(default=timezone.now)
     slug = models.SlugField()

     def __str__(self):
          return self.title 
     
     # def get_absolute_url(self):
     #    return reverse("todo-detail", kwargs={"slug": self.slug})
     
     def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)




