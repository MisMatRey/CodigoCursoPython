def sum_elementos(lista):
    result = 0
    for i in lista:
        result = i + result
    return result

lista1 = [1,2,3,4,5]
print(lista1)
print("El resultado de la lista es : {} ".format(sum_elementos(lista1)))
