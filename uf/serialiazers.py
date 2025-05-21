from rest_framework import serializers
from .models import UF

# Establece el serializador para la clase UF 
class UFSerializer(serializers.ModelSerializer):
    class Meta:
        model = UF
        fields = ['date', 'value']
        
