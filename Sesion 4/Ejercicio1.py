class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Carrito:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(Producto(producto[0],producto[1]))
    
    def muestra_carrito(self):
        for objeto in self.productos:
            print("Producto {} con costo {}".format(objeto.nombre,objeto.precio))

    def monto_total(self):
        tot_lista = 0
        for producto in self.productos:
            tot_lista += producto.precio
        return tot_lista

carrito = Carrito()

carrito.agregar_producto(["Manzanas", 100])
carrito.agregar_producto(["Refresco", 200])
carrito.agregar_producto(["Galletas", 500])

carrito.muestra_carrito()

print("El monto total del Carrito = {}".format(carrito.monto_total()))