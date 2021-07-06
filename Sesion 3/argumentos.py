#arg

def saluda (*nombres, simbolo = "°"):
    for nombre in nombres :
        print("Hola {} {}".format(nombre,simbolo))

saluda("Fernado", "Leonardo", "Misael", simbolo = "!!")

saluda("Fernado", "Leonardo", "Misael")

print("Fernado", "Roman", "Niño")


