import csv
import io

from argparse import ArgumentParser

parser = ArgumentParser()

# Agregando las diferentes opciones de mi linea de comandos
parser.add_argument("-c", "--codigopostal", help="Activa logs en modo desarrollo")

parser.add_argument("-d", "--delegacion", help="Indica la operacion matematica")

# Leyendo los argumentos y parsearlos respecta ^^
args = parser.parse_args()

codigo = args.codigopostal

delegacion = args.delegacion

with io.open("archivos/codigos_postales_cdmx.csv", "r",encoding="utf-8") as archivo:
  # Leyendo y parseando el archivo (interpretando las comas)
  reader = csv.reader(archivo)

  if codigo  != "":
    for linea in reader:
      if linea[0] == codigo and linea[2] == "Colonia":
          print(linea)
  elif delegacion != "":
    for linea in reader:
      if linea[3] == delegacion and linea[2] == "Colonia":
          print(linea)


