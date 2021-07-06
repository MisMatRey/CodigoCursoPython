def suma_numeros(*numeros):
    num_total = 0
    for i in numeros :
        num_total = num_total + i
    return num_total

resultado = 0

print(suma_numeros(1,2,3,4,5))

