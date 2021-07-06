from typing import ValuesView


def calculo(*valores,oper = "+"):
    resultado = 0
    for val in valores :
        if oper == "+" :
            resultado = resultado + val
        elif oper == "-" :
            if resultado == 0:
                resultado = val
            else :
                resultado = resultado - val
        else :
            if resultado == 0 :
                resultado = 1
            resultado = resultado * val
    return resultado

print("La Suma de los numeros = {}".format(calculo(1,2,3,4,5)))

print("La Resta de los numeros = {}".format(calculo(1,2,3,4,5, oper = "-")))

print("La Multiplicacion de los numeros = {}".format(calculo(1,2,3,4,5, oper = "*")))

