from django.forms import *
from .models import *

class ToDoForm(ModelForm):
    
    class Meta:
        model = ToDo
        fields = ('title','descriptions')
        widgets = {
            'title' : TextInput(attrs={'class':'form-control ' ,'placeholder':'Title'}),
            'descriptions' : Textarea(attrs={'class':'form-control form-control form-control-lg ','placeholder':'Descriptions'}),
        }
