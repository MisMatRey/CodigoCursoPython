class Carrito():
    def __init__(self):
        pass

class Refresco():
    def __init__(self, nombre, precio, sabor, presentacion, etiquetas):
        self.nombre =  nombre
        self.precio = precio
        self.sabor = sabor
        self.presentacion = etiquetas

class Moneda:
    def __init__(self, valor = 1 ):
        self.valor = valor

#Agregacion: Reutilizar objetos dentro de otros objetos.
class Monedero:
    monedas = [Moneda(10), Moneda(5), Moneda(2)]

monederito = Monedero()
print(monederito.monedas)