from django.contrib import admin
from .models import Tasks, PropertyTasks

admin.site.register(Tasks)
admin.site.register(PropertyTasks)
class PostModelAdmin(admin.ModelAdmin):
    search_fields = ('staff', 'client', 'works')
