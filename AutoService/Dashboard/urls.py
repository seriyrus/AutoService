from django.urls import path
from . import views

app_name = 'Dashboard'

urlpatterns = [
    path('', views.Dashboard, name='Dashboard'),
    path('createTask', views.createTask, name='createtask'),
    path('AllTask', views.AllTasks, name='AllTask'), 
    path('task/<int:pk>/', views.checkTask, name='checkTask')
]