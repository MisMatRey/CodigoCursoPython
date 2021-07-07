"""
    Las Clases son unas plantillas que describe un objeto (entidad, modelo, cosa)
"""
# Pascal Case
class MiPrimerClase:
    pass 

"""
    Los objetos son las instancias de una clase.

    Instancia  -->>  Referencia de Memoria.
"""
# Came Case
miPrimerObjeto = MiPrimerClase()

#print(miPrimerObjeto)

class Moneda1:
    # atributos (propiedades)
    valor = 1

class Moneda2:
    # atributos (propiedades)
    valor = 2

class Moneda5:
    # atributos (propiedades)
    valor = 5

class Moneda10:
    # atributos (propiedades)
    valor = 10

moneda1 = Moneda1()

# Notacion punto -> Acceder atributos o métodos (objeto.algo)
print(moneda1.valor)

class Moneda:
    """
        El constructor es una clase en una funcion especial 
        que se ejecuta SIEMPRE al momento de crear
        una instacia del objeto
    """
    def __init__(self, valor):
        print("Ejecutando el constructor de la Clase Moneda")
        self.valor = valor  #Creando el atributo "valor" con un valor ingresado en el ejemplo 10 

moneda10 = Moneda(10)

print(moneda10.valor)

