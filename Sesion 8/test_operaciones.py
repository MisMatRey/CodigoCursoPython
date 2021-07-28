from operaciones import *

def test_suma_cero():
    resultado = suma(0,0)
    # Espero que el resultado es 0
    assert resultado == 0

def test_suma_numeros_iguales():
    assert suma(2,2) == 2 * 2
    assert suma(8, 8) == 8 * 2
    assert suma(1000,200) == 2000

def test_suma_cadena():
    resultado = suma("Hello ", "World!!")
    assert len(resultado) > 0
    assert type(resultado) == str
    assert resultado == "Hello World!!"