from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import UF

class UFViewsTest(APITestCase):
    def setUp(self):
        UF.objects.create(date='2025-05-20', value=35000.0)
    
    # Testeamos la API de inicio
    def test_home_endpoint(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK) # Verificamos que la respuesta sea exitosa
        self.assertIn("message", response.data)
        
    # Testeamos la API de listar UF
    def test_uf_list_endpoint(self):
        url = reverse('uf_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK) # Verificamos que la respuesta sea exitosa
        self.assertEqual(len(response.data), 1)
        
    # Testeamos la API de calcular el precio de la UF en pesos chilenos
    def test_uf_price_endpoint(self):
        url = reverse('uf_price')
        response = self.client.get(url, {'value': 10, 'date': '20250520'})
        self.assertEqual(response.status_code, status.HTTP_200_OK) # Verificamos que la respuesta sea exitosa
        self.assertIn("pesos", response.data)
        
    # Testeamos la API de calcular el precio con una fecha que no existe
    def test_uf_price_invalid_date(self):
        url = reverse('uf_price')
        response = self.client.get(url, {'value': 10, 'date': '202505101'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
        
    # Testeamos la API de calcular precio con parámetros inválidos
    def test_uf_price_invalid_params(self):
        url = reverse('uf_price')
        response = self.client.get(url, {'value': 'invalid', 'date': 'params'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
