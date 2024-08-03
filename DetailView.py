from django.views.generic import DetailView

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
