# archivo: test_calculadora.py

from calculadora import sumar

def test_sumar_dos_numeros():
    assert sumar(2, 3) == 5

def test_sumar_con_negativos():
    assert sumar(-1, -1) == -2

def test_sumar_con_cero():
    assert sumar(0, 5) == 5

def test_sumar_con_cero_2():
    assert sumar(0, 0) == 0