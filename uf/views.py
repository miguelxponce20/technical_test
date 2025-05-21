from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UF
from .serialiazers import UFSerializer
import requests
from datetime import datetime

# Realiza la consulta a la API y guarda los datos en la base de datos 
def fetch_uf_data():
    url = 'https://mindicador.cl/api/uf' # URL de la API
    response = requests.get(url)
    if response.status_code == 200: # Verificamos que la respuesta es exitosa
        data = response.json()
        for item in data['serie']:
            date_str = item['fecha'][:10] # Extrae la fecha en formato YYYY-MM-DD y obtiene los primeros 10 caracteres
            date = datetime.strptime(date_str, '%Y-%m-%d').date() # Convierte la fecha a un objeto datetime
            UF.objects.update_or_create(date=date, defaults={'value': item['valor']}) # Actualiza o crea el objeto UF en la DB
            
@api_view(['GET'])
def uf_list(request):
    ufs = UF.objects.all().order_by('date') # Obtenemos todos los objetos UF de la DB y los ordenamos por fecha 
    serializer = UFSerializer(ufs, many=True) # Serializamos los datos
    return Response(serializer.data) 

@api_view(['GET'])
def uf_price(request):
    try:
        value = float(request.GET.get('value'))
        date_str = request.GET.get('date')
        date = datetime.strptime(date_str, '%Y%m%d').date()
    except ValueError:
        return Response({'error': 'Invalid Parameters'}, status=400) # Retornamos un error si los parámetros son inválidos

    try:
        uf = UF.objects.get(date=date) 
        price = value * uf.value # Calculamos el precio
        return Response({'pesos': round(price, 2)}) 
    except UF.DoesNotExist:
        return Response({'error': 'Date not found'}, status=404) # Retornamos un error si la fecha no existe 
    
# Api para la página de inicio
# Esta API retorna un mensaje de bienvenida y los endpoints disponibles
@api_view(['GET']) 
def home(request):
    return Response({
        "message": "Welcome to the UF microservice 👋",
        "endpoints": {
            "Listar UF históricas": "http://127.0.0.1:8000/uf/list?format=api",
            "Calcular valor en CLP": "http://127.0.0.1:8000/uf/price?value=10&date=20250520"
        }
    })