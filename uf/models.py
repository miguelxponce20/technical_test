from django.db import models

# Creamos el modelo UF para almacenar los datos de la API 
class UF(models.Model):
    date = models.DateField(unique=True)
    value = models.FloatField()
    
    def __str__(self):
        return f"UF on {self.date}: {self.value}"
    
    