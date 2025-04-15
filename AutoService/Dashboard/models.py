from django.db import models
from Staff.models import Staffs
from clients.models import Clients
from Property.models import Property

class PropertyTasks(models.Model):
    prop = models.ForeignKey(Property, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.prop.prop_name} - {self.count}"
    
    
    
class Tasks(models.Model):
    
    CHOISES = (
        ('active','Активная'),
        ('created','Созданная'),
        ('complete','Завершенная'),
    )

    staff = models.ForeignKey(Staffs ,on_delete=models.SET_NULL, blank=True, null=True)
    client = models.ForeignKey(Clients, on_delete=models.SET_NULL, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    mode = models.CharField(max_length=100, choices=CHOISES, default='created', blank=True, null=True)
    works = models.CharField(max_length=500, default="", blank=True, null=True)
    time = models.TimeField(auto_now_add=True)
    props = models.ManyToManyField(PropertyTasks, blank=True)
    def __str__(self):
        return f"{self.client} {self.staff} {self.mode}"
    