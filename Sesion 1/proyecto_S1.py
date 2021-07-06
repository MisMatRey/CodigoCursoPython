print(" = = = Calculadora de interes = = = ")

#Ingreso de datos Variables
print("Ingresa el Nombre de la Tarjeta : ") 
str_NombreTj = input()

print("Ingresa la Tasa de Interes : ") 
str_Interes = input()
flo_Interes = float(str_Interes)

print("Ingresa la Deuda : ") 
str_Deuda = input()
flo_Deuda = float(str_Deuda)

print("Ingresa el Pago a Realizar : ") 
str_Pago = input()
flo_Pago = float(str_Pago)

print("Ingresa los Nuevos Cargos : ") 
str_Cargos = input()
flo_Cargos = float(str_Cargos)


#Reporte del resumen y calculos

if flo_Deuda <  flo_Pago :
    print("El Pago no puede ser Mayor a la Deuda -> {} > {}".format(str_Pago,str_Deuda))
else :
    print("Los datos Calculados de la Tarjeta : {}".format(str_NombreTj))
    flo_InteMensual = flo_Interes / 12
    print("El Interes Mensual es = {:5.2f} ".format(flo_InteMensual))
    
    flo_DedaRecal = (flo_Deuda- flo_Pago)*(1+flo_InteMensual)
    print("La Deuda Recalculada = {:10.2f} ".format(flo_DedaRecal))

    print("La Nueva Deuda Resultante = {:10.2f} ".format(flo_DedaRecal + flo_Cargos))

