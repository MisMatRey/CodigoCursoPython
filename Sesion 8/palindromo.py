
def es_palindromo(cadena):
    caracteres = cadena.lower().replace(" ","") 
    return caracteres == caracteres[::-1]