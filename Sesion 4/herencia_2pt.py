class Producto:
    def __init__(self, nombre, precio, etiquetas):
        self.nombre = nombre
        self.precio = precio
        self.etiquetas = etiquetas

    def __str__(self) -> str:
        return "{} - ${}".format(self.nombre, self.precio)

class Refresco(Producto):
    def __init__(self, sabor, nombre, precio, etiquetas):
        super().__init__(nombre, precio, etiquetas)
        self.sabor = sabor
    
    def __str__(self):
        return "Refresco sabor {} -> {}".format(self.sabor,super().__str__())

class Helado(Producto):
    def __init__(self, sabor, presentacion, nombre, precio, etiquetas):
        super().__init__(nombre, precio, etiquetas)
        self.sabor = sabor
        self.presentacion = presentacion


print(Refresco("Cola", "Coca Cola", 15, 2))
