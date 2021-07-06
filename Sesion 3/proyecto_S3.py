from CalculadoraIntereses import tarjeta as trj

# CUERPO DE PROGRAMA

print(" = = = Calculadora de interes = = = ")

# Generacion de Tarjetas
print("Creacion  de Lista 1 ")
lst_tarjetas = list()

dic_Tar1 = trj.crea_tarjeta()

# Calculo Deuda
dic_Tar1 = trj.captura_nueva_deuda(dic_Tar1)

lst_tarjetas.append(dic_Tar1)

#print(" Ingreso de Lista 2 ")
#dic_Tar2 = crea_tarjeta()
#dic_Tar2 = captura_nueva_deuda(dic_Tar2)
#lst_tarjetas.append(dic_Tar2)

# Imprime Tarjetas
#generar_reporte(dic_Tar1)

#barre_listas(lst_tarjetas)

trj.pago_recurrente(dic_Tar1)