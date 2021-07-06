dic_persona = {"nombre" : "Misael", "edad" : 30, "vacunado" : False}

print(dic_persona["nombre"])

print(dic_persona)

dic_persona["nombre"] = "Leonardo"
print(dic_persona)

del dic_persona["vacunado"]

print(dic_persona)

#Agregar una llave

dic_persona["direccion"] = "Casa Principal"

print(dic_persona)

dic_persona.items
dic_persona.keys
dic_persona.items