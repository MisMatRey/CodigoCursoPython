class Moneda:
    def __init__(self, valor = 1):
        self.valor = valor  #Creando el atributo "valor" con un valor ingresado en el ejemplo 10 

    # Ayuda a dar formato o una interpretacion
    def __str__(self):
        return "${}".format(self.valor)

# Agregacion : Reutiliza objetos dentro de otros objetos
class Monedero:
    
    def __init__(self) -> None:
        self.monedas = []

    # Accion (metodo)
    def agregar_moneda(self, valor) :
        self.monedas.append(Moneda(valor))
    
    def ver_monedas(self):
        for moneda in self.monedas :
            print(moneda)
    
    def monto_total(self):
        total = 0
        for moneda in self.monedas:
            total = total + moneda.valor
        return total

monederito = Monedero()

monederito.agregar_moneda(10)
monederito.agregar_moneda(5)
monederito.agregar_moneda(20)

monederito.ver_monedas()

print(monederito.monto_total())

