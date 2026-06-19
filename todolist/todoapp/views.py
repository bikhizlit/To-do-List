from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'todoapp/todo.html', {'tasks': tasks})


def add_todo(request):
    if request.method == "POST":
        task_title = request.POST.get("title")
        task_category = request.POST.get("category")
        
        if task_title:  
            new_task = Task(title=task_title, category=task_category)
            new_task.save()
            
    return redirect('task_list')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')




def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        new_title = request.POST.get("title")
        if new_title:
            task.title = new_title
            task.save()
        return redirect('task_list')
    return redirect('task_title')
    



def clear_all_tasks(request):
    Task.objects.all().delete()
    return redirect('task_list')


    