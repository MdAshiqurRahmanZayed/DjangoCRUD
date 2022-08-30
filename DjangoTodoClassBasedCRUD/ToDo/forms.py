from django import forms 
from .models import *

class TodoForm(forms.ModelForm):

    
     class Meta:
        model = Todo
        fields = ('title','descriptions')
        
     widgets = {
          'title' : forms.TextInput(attrs={'class':'form-control form-control form-control-lg '}),
          'descriptions' : forms.Textarea(attrs={'class':'form-control ' ,'placeholder':'descriptions'})
     }
