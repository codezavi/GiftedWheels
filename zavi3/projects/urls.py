from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),
    path('create-project/', views.createproject, name="create-project"),
    path('update_project/<str:pk>/', views.updateproject, name="update_project"),
    path('delete_project/<str:pk>/', views.deleteproject, name="delete_project"),
]