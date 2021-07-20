from sys import argv

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


argumentos = argv[2:]

operacion = argv[1]


numeritos = []

for numero in argumentos :
    numeritos.append(int(numero))

if operacion ==  "+" :
    print(suma(*numeritos))
elif operacion ==  "-" :
    print(resta(*numeritos))   
else :
    print("Operacion no permitida")
