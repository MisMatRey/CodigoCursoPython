import re

class Producto:
  def __init__(self, nombre, precio):
    self.nombre = nombre
    self.precio = precio

  def __str__(self):
    return "{} - ${}".format(self.nombre, self.precio)


def carga_inventario():
  lista = []
  with open("archivos/inventario.txt","r") as archivo :
    for linea in archivo:
      argumentos = linea.split('|')
      lista.append(Producto(argumentos[0],re.sub("\n","",argumentos[1])))
  return lista

def guarda_inventario(nombre,precio):
  with open("archivos/inventario.txt","a") as archivo : 
    archivo.write("{}|{}\n".format(nombre,precio))

inventario = []

# 1. Cargar el inventario del archivo "inventario.txt"
# 2. Almacenar el inventario en el mismo archivo

salir = False

inventario = carga_inventario()

#print(inventario)

while not salir:
  print("\n")
  print("1. Agregar productos")
  print("2. Lista de productos")
  print("3. Salir")

  opcion = input()

  print("\n")

  if opcion == "2":
    for producto in inventario:
      print(producto)
  elif opcion == "1":
    print("Ingresa el nombre:")
    nombre = input()
    print("Ingresa el precio:")
    precio = input()

    inventario.append(Producto(nombre, precio))
    guarda_inventario(nombre,precio)

    print("\nProducto agregado")
  elif opcion == "3":
    salir = True
  else:
    print("Opción inválida")

print("Cerrrando sistema")
