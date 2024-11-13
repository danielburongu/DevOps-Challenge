# tasks/views.py
from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django.http import HttpResponse

# View for the Task API
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Define the home view
def home(request):
    return HttpResponse("Welcome to my to-do API")
