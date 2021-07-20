from sys import argv
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("-d", "--debug", help="Activa logs para Desarrollador",action="store_true")

parser.add_argument("-o", "--operacione", help="Operacion a realizar",default="+")

parser.add_argument("-n", "--numeros", help="Lista de Numeros a operar")

args =  parser.parse_args()

def suma(*numeros):
    resultado = 0
    for numero in numeros :
        resultado += numero
    return resultado

def resta(*numeros):
    resultado = numeros[0]
    for numero in numeros[1:] :
        resultado -= numero
    return resultado

def multiplicacion(*numeros):
    resultado = 1
    for numero in numeros :
        resultado *= numero
    return resultado


argumentos = args.numeros

operacion = args.operacione

numeritos = []

for numero in argumentos :
    numeritos.append(int(numero))

if operacion ==  "+" :
    print(suma(*numeritos))
elif operacion ==  "-" :
    print(resta(*numeritos))   
else :
    print("Operacion no permitida")
