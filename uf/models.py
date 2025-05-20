from django.db import models

# Create your models here.
class UF(models.Model):
    date = models.DateField(unique=True)
    value = models.FloatField()
    
    def __str__(self):
        return f"UF on {self.date}: {self.value}"
    
    