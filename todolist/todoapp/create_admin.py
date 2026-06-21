import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todolist.settings') # Replace 'your_project_name' with your actual project folder name
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
username = 'renderadmin'  # Choose your username
email = 'admin@example.com'
password = '11111111' # Choose a strong password

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Superuser created successfully!")
else:
    print("Superuser already exists.")