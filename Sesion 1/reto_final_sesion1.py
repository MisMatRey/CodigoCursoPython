print("Ingresa el Numero 1 :")
val1 = input()

print("Ingresa el Numero 2 :")
val2 = input()

print ("Que operacion quieres realizar :")
print ("+ -> Suma ")
print ("- -> Resta ")
print ("* -> Multiplicacion ")
print ("/ -> Division ")
print ("% -> Modulo")
val3 = input()

#Casteo de tipos

num1 = int(val1)
num2 = int(val2)

if val3 ==  "+" :
    print("{} + {} = {}".format(num1,num2,num1 + num2))
elif  val3 ==  "-" :
    print("{} - {} = {}".format(num1,num2,num1 - num2))
elif  val3 ==  "*" :
    print("{} * {} = {}".format(num1,num2,num1 * num2))
elif  val3 ==  "/" :
    if num2 == 0 :
        print("Division no permitida")
    else :
        print("{} / {} = {}".format(num1,num2,num1 / num2))
elif  val3 ==  "%" :
    print("{} % {} = {}".format(num1,num2,num1 % num2))
else :
    print("Operacion no permitida")
