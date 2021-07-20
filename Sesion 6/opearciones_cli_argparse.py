from argparse import ArgumentParser

parser = ArgumentParser()

# Agregando las diferentes opciones de mi linea de comandos
parser.add_argument("-d", "--debug", help="Activa logs en modo desarrollo", action="store_true")

parser.add_argument("-o", "--operacion", help="Indica la operacion matematica",  default="+")

parser.add_argument("-n", "--numeros", help="Lista de numeros a operar")

# Leyendo los argumentos y parsearlos respecta ^^
args = parser.parse_args()

def print_debug(mensaje):
  if args.debug:
    print(mensaje)

def suma(*numeros):
  print_debug("Ejecutando la suma")
  resultado = 0
  for numero in numeros:
    resultado = resultado + numero
  return resultado

def resta(*numeros):
  print_debug("Ejecutando la resta")
  resultado = numeros[0]
  for numero in numeros[1:]:
    resultado = resultado - numero
  return resultado

def multiplicacion(*numeros):
  print_debug("Ejecutando la multiplicacion")
  resultado = 1
  for numero in numeros:
    resultado = resultado * numero
  return resultado

def division(*numeros):
  print_debug("Ejecutando la division")
  resultado = numeros[0]
  try:
    for numero in numeros[1:]:
      resultado = resultado / numero
    return resultado
  except ZeroDivisionError:
    print("Error: División por 0")
    return 0

argumentos = args.numeros

operacion = args.operacion

# Divido los numeros por una coma: "1,2,3" -> ["1","2","3"]
argumentos_split = argumentos.split(",")

# Convierte cada texto en un numero
numeritos = []
for argumento in argumentos_split:
  numeritos.append(int(argumento))

if operacion == "+":
  print(suma(*numeritos))
elif operacion == "-":
  print(resta(*numeritos))
elif operacion == "*":
  print(multiplicacion(*numeritos))
elif operacion == "/":
  print(division(*numeritos))
else:
  print("Operación invalida")