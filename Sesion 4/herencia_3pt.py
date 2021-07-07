class Producto:
  def __init__(self, nombre, precio, etiquetas, ingredientes):
    self.nombre = nombre
    self.precio = precio
    self.etiquetas = etiquetas
    self.ingredientes = ingredientes

  def cualquier_metodo(self):
    print("Soy cualquier metodo de Producto")

  def __str__(self):
    return "{} - ${}".format(self.nombre, self.precio)

class Refresco(Producto):
  def __init__(self, sabor, nombre, precio, etiquetas, ingredientes):
    super().__init__(nombre, precio, etiquetas, ingredientes)
    self.sabor = sabor

  def __str__(self):
      return "Refresco sabor {} -> {}".format(self.sabor, super().__str__())

  def cualquier_metodo(self):
      print("Soy cualquier metodo de refresco")
      super().cualquier_metodo()

class Helado(Producto):
  def __init__(self, sabor, presentacion, nombre, precio, etiquetas, ingredientes):
    super().__init__(nombre, precio, etiquetas, ingredientes)
    self.sabor = sabor
    self.presentacion = presentacion

class Tortillas(Producto):
  def __init__(self, cantidad, nombre, precio, etiquetas, ingredientes):
    super().__init__(nombre, precio, etiquetas, ingredientes)
    self.cantidad = cantidad

class CualquierClase(Refresco):
  #def __init__(self, sabor, nombre, precio, etiquetas, ingredientes):
  #  super().__init__(nombre, precio, etiquetas, ingredientes)
  #  self.sabor = sabor
  def cualquier_metodo(self):
      print("Soy cualquier metodo de cualquier clase")
      super().cualquier_metodo()

      
print(Refresco("Cola", "Coca Cola", 15, 4, "Cancer"))
CualquierClase("Cola", "Coca Cola", 15, 4, "Cancer").cualquier_metodo()