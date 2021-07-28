import py
from vocales_unicas import vocales
import pytest

@pytest.mark.parametrize('cadena, vocal',[("a",["a"]),("m",[]),("E",["e"]),("Z",[])])
def test_un_caracter(cadena,vocal):
    assert vocales(cadena) == vocal

@pytest.mark.parametrize('cadena, vocal',[("ab",["a"]),("bm",[]),("zE",["e"]),("ae",["a","e"])])
def test_dos_caracteres_ordenados(cadena, vocal):
    assert vocales(cadena) == vocal

@pytest.mark.parametrize('cadena, vocal',[("Casa",["a"]),("tere",["e"]),("bahia",["a","i"]),("te pide",["e","i"])])
def test_vocales_repetidas(cadena, vocal):
    assert vocales(cadena) == vocal

@pytest.mark.parametrize('cadena, vocal',[("Hola mundo",["a","o","u"]),("Casa perdida",["a","e","i"]),("Complidado tu de ver",["a","e","i","o","u"])])
def test_cadenas_complejas(cadena, vocal):
    assert vocales(cadena) == vocal
