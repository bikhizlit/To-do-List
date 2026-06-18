from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    if request.method == "POST":
        #Get the title from the form input (name="title")
        task_title = request.POST.get("title")
        
        if task_title:  
            #Force create and immediately save to the database
            new_task = Task(title=task_title)
            new_task.save()
            
        return redirect('task_list')

    #Fetch all tasks to display on the page
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'todoapp/todo.html', {'tasks': tasks})

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


    