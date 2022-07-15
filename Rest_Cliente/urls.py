from django.urls import path 
from .views import lista_clientes

urlpatterns= [ 
    path('lista_clientes', lista_clientes, name="lista_clientes"),
]