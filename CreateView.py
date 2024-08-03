from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category']


from django.views.generic.edit import CreateView
from .forms import TaskForm

class TaskCreateView(CreateView):
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = '/tasks/'
