from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Router to automatically create routes for the TaskViewSet
router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
