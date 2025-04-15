from django.db import models
from colorfield.fields import ColorField

class Staffs(models.Model):
    
    COLOR_PALETTE = [
        ("#FFFFFF", "white", ),
        ("#000000", "black", ),
    ]
    
    staff_job = models.CharField(max_length=40, blank=True, null=True)
    staff_surname = models.CharField(max_length=150, blank=True, null=True)
    staff_name = models.CharField(max_length=150, blank=True, null=True)
    color = ColorField(samples=COLOR_PALETTE, blank=True, null=True)
    
    def __str__(self):
        return f'{self.staff_name} {self.staff_surname} {self.staff_job}'
