from django.contrib import admin
from .models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'completed', 'created_at') # Columns you want to see

# This officially registers the model into the admin panel
admin.site.register(Task, TaskAdmin)
