"""

   Modulo para la Clase Tarjeta y los metodos para el uso de las tarjetas y proyeccion sobre las mismas.

"""
class Tarjeta:
    """
        Clase para definir los Atributos y Metodos de las Tarjetas.
    """
    nombre = ""
    numero = 0
    tasa = 0.0
    deuda = 0.0
    pago = 0.0
    cargo = 0.0

    def __init__(self, nombre):
        self.nombre = nombre

    def crea_tarjeta(self) :
        """
           Funcion que crea una tarjeta e ingresa los datos de la misma.
        """
        
        #Ingreso de datos Variables
        if self.nombre == "" :
            print("Ingresa el Nombre de la Tarjeta : ") 
            self.nombre = input()
            
        print("Ingresa la Tasa de Interes : ") 
        str_Interes = input()
        self.tasa = float(str_Interes)/100
    
        print("Ingresa la Deuda : ") 
        str_Deuda = input()
        self.deuda =  float(str_Deuda)
    
        print("Ingresa el Pago a Realizar : ") 
        str_Pago = input()
        self.pago =  float(str_Pago)
    
        while self.deuda < self.pago :
            print("Pago mayor a la Deuda {}. Ingresa Nuevo Pago a Realizar : ".format(dic_Tarjeta["Deuda"])) 
            str_Pago = input()
            dic_Tarjeta["Pago"] =  float(str_Pago)
        
        print("Ingresa los Nuevos Cargos : ") 
        str_Cargos = input()
        dic_Tarjeta["Cargos"] = float(str_Cargos)
    
        return dic_Tarjeta

def captura_nueva_deuda(dic_TarjCal):
    """
       Funcion que complemente los calculos de la tarjeta con la Deuda Resultante.
    """
    
    flo_InteMensual = dic_TarjCal["Tasa"] / 12
    
    flo_DedaRecal = (dic_TarjCal["Deuda"] - dic_TarjCal["Pago"] )*(1+flo_InteMensual)
    
    dic_TarjCal["Deuda_Resultante"] = flo_DedaRecal + dic_TarjCal["Cargos"]

    #print(dic_TarjCal)
    #print(type(dic_TarjCal))

    return dic_TarjCal

def generar_reporte(dic_TarjRepo) :
    """
       Funciones que Genera el Reporte con los datos de la Tarjeta.
    """
    
    print("Los datos Calculados de la Tarjeta : {}".format(dic_TarjRepo["Nombre"]))
    
    print("El Interes Mensual es = {:5.2f} ".format(dic_TarjRepo["Tasa"]))
    
    print("La Deuda Actual = {:10.2f} ".format(dic_TarjRepo["Deuda"]))

    print("Pago a Realizar = {:10.2f} ".format(dic_TarjRepo["Pago"]))

    print("La Nueva Deuda Resultante = {:10.2f} ".format(dic_TarjRepo["Deuda_Resultante"]))

def barre_listas(rcv_Tarjetas):
    """
       Funciones que Barre una lista de Tarjetas y manda a imprimir sus reportes.
    """
    for elemento in rcv_Tarjetas :
        generar_reporte(elemento)

def pago_recurrente(dts_Tarjeta):
    """
       Funciones que genera el reporte de los pagos recurrentes de una Tarjeta.
    """
    int_mes = 1
    dts_Proyeccion = dts_Tarjeta

    print(" = = =  Proyeccion de Pagos mensuales  = = = ")

    dts_Tarjeta.values()
    dts_Proyeccion.values()

    if dts_Proyeccion["Deuda"] < dts_Proyeccion["Deuda_Resultante"] :
        print("La Deuda Resultante es mayor a la Deuda Actual, no se puede proyectar.")
        generar_reporte(dts_Proyeccion)
    else : 
        while dts_Proyeccion["Deuda_Resultante"] > 0:
            print("Reporte mes {}.".format(int_mes))
            generar_reporte(dts_Proyeccion)
            dts_Proyeccion["Deuda"] = dts_Proyeccion["Deuda_Resultante"]
            dts_Proyeccion = captura_nueva_deuda(dts_Proyeccion)
            int_mes += 1
        dts_Proyeccion["Deuda_Resultante"] = 0
        dts_Proyeccion["Pago"] = dts_Proyeccion["Deuda"]
        print("Reporte mes {}.".format(int_mes))
        generar_reporte(dts_Proyeccion)
