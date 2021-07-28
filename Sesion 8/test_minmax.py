import py
from minmax import min_max
import pytest

@pytest.mark.parametrize('digito',[0,4,-1])
def test_un_numero(digito):
    assert min_max(digito) == {"min":digito, "max":digito}

@pytest.mark.parametrize('a, b', [(0,1),(5,10), (-100, -20)])
def test_dos_numeros_ordenados(a, b):
    assert min_max(a,b) == {"min":a, "max":b}

def test_dos_numeros_desordenados():
    assert min_max(5,3) == {"min":3, "max":5}
    assert min_max(100,20) == {"min":20, "max":100}
    assert min_max(-10,-200) == {"min":-200, "max":-10}


def test_cualquier_cantidad():
    assert min_max(1,2,3,4,5,6,7,8,9) == {"min":1, "max":9}
    assert min_max(800, 60, 32, 25, 12,20) == {"min":12, "max":800}
    assert min_max(1,1,1,1,1,1,1,1,1,1) == {"min":1, "max":1}
    assert min_max(-300, -10, -25, -60, -200) == {"min":-300, "max":-10}