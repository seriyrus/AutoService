from django.urls import path
from . import views

app_name='Staff'

urlpatterns = [
    path('', views.Staff, name='Staff'),
]