print ("Ingresa el numero :")
dat1 = input()

num1 = int(dat1)

if num1 < 0 :
    print("Numero negativo")
    if num1 == -1 :
        print("Numero -1")
elif  num1 > 0 :
    print("Numero positivo")
else :
    print("Numero 0")
