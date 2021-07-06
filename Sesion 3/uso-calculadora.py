#importar archivo o funcion
#import calculadora 

# 1ra Forma de importar todo el archivo
import calculadora as cal

print(cal.suma(1,5))
print(cal.resta(5,1))
print(cal.multiplicacion(1,5))

# 2da forma de importar una o varias funciones
from calculadora import division, multiplicacion

print(division(4,0))

print(multiplicacion(3,2))

#3ra forma 

from calculadora import *

print(suma(3,2))