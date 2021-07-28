
def vocales(cadena):
    texto = sorted(cadena.lower())
    vocales = []
    tamaño = len(texto)
    
    for caracter in texto :
        #print(caracter)
        if caracter in "aeiou":
            if caracter not in vocales :
                vocales = vocales + [caracter]
        
    return vocales

#print(vocales("ae"))