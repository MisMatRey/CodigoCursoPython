import csv

# Escritura de un archivo CSV
with open("archivos/padron_electoral_fake.csv", "a", newline="") as archivo:
  writer = csv.writer(archivo)
  writer.writerow([])
  writer.writerow(["Juan Perez", "40", "Avenida Reforma #223, Cuauhtemoc"])

# Lectura de un archivo CSV
with open("archivos/padron_electoral_fake.csv", "r") as archivo:
  # Leyendo y parseando el archivo (interpretando las comas)
  reader = csv.reader(archivo)
  for linea in reader:
    print(linea)
