import sys

#print("Hello World!!")
"""
    sys.argv es una lista con todos los argumentos de la linea de comandos

    nota: el primer argumento siempre es el nombre del archivo. (argv[0])
"""
#print("Ejecuntando: ",sys.argv[0])

#print(sys.argv)

#numero1 = int(sys.argv[1])
#numero2 = int(sys.argv[2])
#numeor3 = int(sys.argv[3])

#print("Resusltado :",numero1+numero2+numeor3)

#print(sys.argv[1:]) #Cortar la lista quitando el nombre del archivo

resultado = 0

for argumento in sys.argv[1:]:
    resultado += int(argumento)

print("La suma de los argumentos : ",resultado)
