from unittest.util import _MAX_LENGTH
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Producto, Cliente

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields=['idProducto','nombre','stock','precio','fechaFabricacion','imagen',]
        labels ={
            'idProducto': 'ID del producto', 
            'nombre': 'Nombre del producto', 
            'stock': 'Stock', 
            'precio' : 'Precio del producto',
            'fechaFabricacion': 'Fecha de fabricacion',
            'imagen': 'Imagen',
            
        }
        widgets={
            'idProducto': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese la id del producto', 
                    'id': 'idProducto'
                }
            ),
            
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre del producto', 
                    'id': 'nombre'
                }
            ), 
            'stock': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'stock', 
                    'id': 'stock'
                }
            ), 
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el precio del producto', 
                    'id': 'precio',
                }
            ),     
            'fechaFabricacion': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la fecha de fabricacion del producto', 
                    'id': 'fechaFabricacion',
                    
                }
            ),
             
        }


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields=['nombre','email','direccion','telefono','contrasena']
        labels ={ 
            'nombre': 'Nombre del cliente', 
            'email': 'Email del cliente',
            'direccion': 'Direccion del cliente',
            'telefono': 'Telefono del cliente',
            'contrasena': 'Ingrese contraseña',
        }
        widgets={
            
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre del cliente', 
                    'id': 'nombre'
                }
            ), 
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el email del cliente', 
                    'id': 'email',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la direccion del cliente', 
                    'id': 'direccion',
                }
            ),
            'telefono': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el telefono del cliente', 
                    'id': 'telefono',
                }
            ),
            'contrasena': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese contraseña', 
                    'id': 'contrasena'
                }
            ), 
        }