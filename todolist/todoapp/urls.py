from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('add/', views.add_todo, name='add_todo'),
    path('toggle-theme/', views.toggle_theme, name='toggle_theme'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('edit/<int:task_id>/', views.edit_task, name="edit_task"),
    path('clear_all/', views.clear_all_tasks, name='clear_all_tasks'),
    

]