# archivo: test_seguridad.py

from seguridad import es_contrasena_segura

def test_contrasena_segura_valida():
    assert es_contrasena_segura("Abcd1234") is True

def test_contrasena_tiene_menos_de_8_caracteres():
    assert es_contrasena_segura("Ab1") is False

def test_contrasena_sin_mayusculas():
    assert es_contrasena_segura("abcd1234") is False

def test_contrasena_sin_minusculas():
    assert es_contrasena_segura("ABCD1234") is False

def test_contrasena_sin_numeros():
    assert es_contrasena_segura("Abcdefgh") is False
