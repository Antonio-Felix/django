from django.urls import path
from .views import lista_filmes

urlpatterns = [
    path('', lista_filmes, name='lista_filmes'),
]
