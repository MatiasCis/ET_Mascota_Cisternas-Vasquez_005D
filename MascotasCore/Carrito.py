from django.contrib.auth.models import User
from datetime import date, datetime

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

class Carrito:
    def __init__(self,request):
        self.session=request.session
        carrito=self.session.get("carrito")
        if not carrito:
            self.session["carrito"]={}
            self.carrito=self.session["carrito"]
        else:
            self.carrito=carrito

    def agregar(self, producto):
        id= str(producto.idProducto)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id":producto.idProducto,
                "nombre":producto.nombre,
                "stock":producto.stock,
                "acumulado":producto.precio,
                "cantidad":1,
            }
        else:
            self.carrito[id]["cantidad"]+=1
            self.carrito[id]["acumulado"] += producto.precio       
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"]=self.carrito
        self.session.modified=True

    def eliminar(self,producto):
        id=str(producto.idProducto)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self,producto):
        id=str(producto.idProducto)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"]-=1
            self.carrito[id]["acumulado"]-=producto.precio
            if self.carrito[id]["cantidad"]<=0: self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True