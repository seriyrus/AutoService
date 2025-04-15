from django.db import models

class Property(models.Model):
    prop_name = models.CharField(max_length=150, blank=True, null=True)
    prop_cost = models.IntegerField(blank=True, null=True)
    prop_col = models.IntegerField(blank=True, null=True)
    prop_allcost =models.IntegerField(null=True, blank=True)
    prop_position = models.CharField(max_length=40, null=True, blank=True)
    
    def __str__(self):
        return f'{self.prop_name}: {self.prop_col}'
