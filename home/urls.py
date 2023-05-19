from django.urls import path
from .import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('temporada/', views.temporada, name='temporada'),
    path('descarga/', views.descarga, name='descarga'),
    path('bloc/', views.bloc, name='bloc'),
    path('contacto/', views.contacto, name='contacto'),
]
