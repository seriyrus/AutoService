from django.db import models

class Clients(models.Model):
    client_surname = models.CharField(max_length=150, blank=True, null=True)
    client_name = models.CharField(max_length=150, blank=True, null=True)
    client_fathername = models.CharField(max_length=150, blank=True, null=True)
    client_phone = models.CharField(max_length=20, blank=True, null=True)
    client_auto = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return f'{self.client_surname} {self.client_name} {self.client_fathername} {self.client_phone}'