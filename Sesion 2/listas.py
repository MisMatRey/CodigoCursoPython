list_vacia = []
list_vacia2 = list()

print(list_vacia)

#lista Poblada
list1 = [100,200,300,400]

#operaciones

#Lectura
print(" Lista1[1] = ")
print(list1[1])

#Agregar elemento

list1 = [800] + list1

#list1.insert(500)
#print(list1)

list1.insert(3, 500)

print(list1)
print(len(list1))

#borrar elemento
del list1[2]
print(list1)

#buscar el indice de un elemento
print(list1.index(400))

#ordenar lista
print(sorted(list1))
