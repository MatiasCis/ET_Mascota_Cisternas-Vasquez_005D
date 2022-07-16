from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id de Producto')
    nombre = models.CharField(max_length=50, verbose_name='Nombre del producto')
    stock=models.IntegerField(verbose_name="Stock")
    precio = models.IntegerField(verbose_name='Precio del producto', null=True)
    fechaFabricacion = models.DateField()
    imagen = models.ImageField(upload_to="Productos", null=True)
   
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    idCliente=models.AutoField(primary_key=True, verbose_name='ID de cliente')
    nombre=models.CharField(max_length=25,verbose_name='Nombre de cliente')
    email=models.CharField(max_length=50, verbose_name='Email de cliente')
    direccion=models.CharField(max_length=25, verbose_name='Direccion de cliente', null=True)
    telefono=models.IntegerField(verbose_name='Telefono de cliente', null=True)
    contrasena=models.CharField(verbose_name='Contraseña', max_length=20, null=True)
    
    def __str__(self):
        return self.nombre


class Venta(models.Model):
    nmr_orden = models.BigIntegerField()
    total = models.IntegerField()
    fch_compra = models.CharField(max_length=40)
    fch_entrega = models.CharField(max_length=40,blank=True, null=True)
    idUser=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    


    
    def __str__(self):
        return str(self.nmr_orden)


class VentaProducto(models.Model):
    cantidad=models.IntegerField()
    orden=models.ForeignKey(Venta,on_delete=models.SET_NULL,null=True)
    producto=models.ForeignKey(Producto,on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return str(self.cantidad)