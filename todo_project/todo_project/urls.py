# todo_project/urls.py
from django.contrib import admin
from django.urls import path, include
from tasks import views as task_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_views.home, name='home'),  # Home page route
    path('api/', include('tasks.urls')),     # API route
]
