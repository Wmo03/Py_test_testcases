# test_validacion.py

from validacion import es_email_valido

def test_email_valido():
    assert es_email_valido("usuario@ejemplo.com") is True

def test_email_sin_arroba():
    assert es_email_valido("usuario.ejemplo.com") is False

def test_email_sin_dominio():
    assert es_email_valido("usuario@") is False

def test_email_con_caracteres_invalidos():
    assert es_email_valido("usu@rio@ejemplo.com") is False

def test_email_con_espacios():
    assert es_email_valido("usuario @ejemplo.com") is False
