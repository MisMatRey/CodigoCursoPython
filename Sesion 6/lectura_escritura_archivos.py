"""
archivo = open("archivos/Hello_word.txt","r")

print(archivo.readline())

archivo.close()
"""

with open("archivos/Arch_salida.txt","w") as archivo : 
    archivo.writelines(["Linea 1 \n","Linea 2 \n","Linea 3 \n"])

with open("archivos/Hello_word.txt","r") as archivo :
    for linea in archivo:
        print(linea)

with open("archivos/Arch_salida.txt","a") as archivo : 
    archivo.write("\n Python")
