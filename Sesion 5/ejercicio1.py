class Dulce():
    codigo = ""
    nombre = ""

    def __init__(self,codigo,nombre) -> None:
        self.codigo = codigo
        self.nombre = nombre

class ListaDulces():
    __dulces = []

    def __init__(self):
        self.__dulces.append(Dulce("A0","Chocolate"))
        self.__dulces.append(Dulce("B1","Chicle"))

    def dame_dulce(self,codigo):
        for dul in self.__dulces:
            if dul.codigo == codigo :
                return dul.nombre
        
        return "S/P"

class MaquinaExpendedora(ListaDulces):

    def __init__(self):
        super().__init__()
    
    def comprar(self, codigo):
        return self.dame_dulce(codigo)


maquina = MaquinaExpendedora()

print(maquina.comprar("A0"))

print(maquina.comprar("B1"))