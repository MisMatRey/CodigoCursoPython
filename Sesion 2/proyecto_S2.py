def crea_tarjeta() :
    
    dic_Tarjeta = {"Nombre" : "", "Tasa" : 0.0, "Deuda" : 0.0, "Pago" : 0.0, "Cargos" : 0.0} 
    #Ingreso de datos Variables
    print("Ingresa el Nombre de la Tarjeta : ") 
    dic_Tarjeta["Nombre"] = input()

    print("Ingresa la Tasa de Interes : ") 
    str_Interes = input()
    dic_Tarjeta["Tasa"] = float(str_Interes)

    print("Ingresa la Deuda : ") 
    str_Deuda = input()
    dic_Tarjeta["Deuda"] =  float(str_Deuda)

    print("Ingresa el Pago a Realizar : ") 
    str_Pago = input()
    dic_Tarjeta["Pago"] =  float(str_Pago)

    while dic_Tarjeta["Deuda"] < dic_Tarjeta["Pago"] :
        print("Pago mayor a la Deuda {}. Ingresa Nuevo Pago a Realizar : ".format(dic_Tarjeta["Deuda"])) 
        str_Pago = input()
        dic_Tarjeta["Pago"] =  float(str_Pago)
    
    print("Ingresa los Nuevos Cargos : ") 
    str_Cargos = input()
    dic_Tarjeta["Cargos"] = float(str_Cargos)

    return dic_Tarjeta

def captura_nueva_deuda(dic_TarjCal):
    
    flo_InteMensual = dic_TarjCal["Tasa"] / 12
    
    flo_DedaRecal = (dic_TarjCal["Deuda"] - dic_TarjCal["Pago"] )*(1+flo_InteMensual)
    
    dic_TarjCal["Deuda_Resultante"] = flo_DedaRecal + dic_TarjCal["Cargos"]

    #print(dic_TarjCal)
    #print(type(dic_TarjCal))

    return dic_TarjCal

def generar_reporte(dic_TarjRepo) :
    
    print("Los datos Calculados de la Tarjeta : {}".format(dic_TarjRepo["Nombre"]))
    
    print("El Interes Mensual es = {:5.2f} ".format(dic_TarjRepo["Tasa"]))
    
    print("La Deuda Actual = {:10.2f} ".format(dic_TarjRepo["Deuda"]))

    print("Pago a Realizar = {:10.2f} ".format(dic_TarjRepo["Pago"]))

    print("La Nueva Deuda Resultante = {:10.2f} ".format(dic_TarjRepo["Deuda_Resultante"]))

def barre_listas(rcv_Tarjetas):
    for elemento in rcv_Tarjetas :
        generar_reporte(elemento)

def pago_recurrente(dts_Tarjeta):
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



# CUERPO DE PROGRAMA

print(" = = = Calculadora de interes = = = ")

# Generacion de Tarjetas
print(" Ingreso de Lista 1 ")
lst_tarjetas = list()

dic_Tar1 = crea_tarjeta()

# Calculo Deuda
dic_Tar1 = captura_nueva_deuda(dic_Tar1)

lst_tarjetas.append(dic_Tar1)

print(" Ingreso de Lista 2 ")
dic_Tar2 = crea_tarjeta()

dic_Tar2 = captura_nueva_deuda(dic_Tar2)

lst_tarjetas.append(dic_Tar2)


# Imprime Tarjetas

#generar_reporte(dic_Tar1)

barre_listas(lst_tarjetas)

pago_recurrente(lst_tarjetas[0])