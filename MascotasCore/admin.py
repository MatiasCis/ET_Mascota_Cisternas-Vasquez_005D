from django.contrib import admin
from django.utils.html import format_html
from .models import *







# Register your models here.

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(VentaProducto)


