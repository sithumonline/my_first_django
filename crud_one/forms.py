from django import forms
from django.forms import ModelForm
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'title': 'Title',
            'description': 'Description',
            'completed': 'Completed',
        }
        help_texts = {
            'title': 'Enter the title of the todo item.',
            'description': 'Enter a brief description of the todo item.',
            'completed': 'Check if the todo item is completed.',
        }
        error_messages = {
            'title': {
                'required': 'This field is required.',
                'max_length': 'This field cannot exceed 200 characters.',
            },
            'description': {
                'required': 'This field is required.',
            },
        }
        # Custom validation
