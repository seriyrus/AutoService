from django.urls import path
from . import views

app_name='Property'

urlpatterns = [
    path('', views.Property, name='Property'),
]