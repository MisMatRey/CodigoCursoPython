def describe_persona (**persona):
    print(type(persona))

    for llave, valor in persona.items() : 
        print(llave, valor)

describe_persona(nombre = "Misael", edad = "30", direccion = "Corindon 1")
