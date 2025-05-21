from django.urls import path
from . import views

# Registramos las rutas de las API
urlpatterns = [
    path('', views.home, name='home'),
    path('uf/list', views.uf_list, name='uf_list'),
    path('uf/price', views.uf_price, name='uf_price'),
]
