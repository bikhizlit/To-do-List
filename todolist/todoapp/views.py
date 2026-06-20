from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Task, Profile

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todoapp/todo.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-created_at')

@login_required
def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        if title:
            Task.objects.create(
                user=request.user, 
                title=title, 
                category=category
            )
    return redirect('task_list')

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        new_title = request.POST.get("title")
        if new_title:
            task.title = new_title
            task.save()
    return redirect('task_list')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('task_list')

@login_required
def clear_all_tasks(request):
    Task.objects.filter(user=request.user).delete()
    return redirect('task_list')

@login_required
def toggle_theme(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    profile.theme = 'dark' if profile.theme == 'light' else 'light'
    profile.save()
    return redirect(request.META.get('HTTP_REFERER', 'task_list'))

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # The signal triggers here and builds the profile flawlessly!
            login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')