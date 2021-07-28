def min_max(*numeros):

    lista_numeros =  sorted(list(numeros))       
    return {"min" : lista_numeros[0], "max" : lista_numeros[-1]}