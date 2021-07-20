class Persona:
    nombre = "Paquito"
    edad = 14
    vacunado = False

    def presentate(self):
        print("Hola me llamo ", self.nombre)


paquito = Persona()

paquito.nombre = "Juanito"

#paquito.presentate()


class CuentaBancaria:

    def __init__(self, monto):
        self.__monto = monto

    def abonar(self, abono):
        self.__monto = self.__monto + abono
    
    def estado_cuenta(self):
        print(self.__monto)
    
    def regresa_monto(self):
        return self.__monto

guardatito = CuentaBancaria(100)

guardatito.abonar(50)

guardatito.__monto = 10000

print(guardatito.__monto)

guardatito.estado_cuenta()


class CuentaPremium(CuentaBancaria):

    def __init__(self):
        super().__init__(150000)
    
    def estado_cuenta_premium(self):
        print("Usuario premiun su estado de cuenta es ", self.regresa_monto())

premium = CuentaPremium()

premium.estado_cuenta()

premium.estado_cuenta_premium()