# test_operaciones.py

from operaciones import calcular_precio_con_iva, puede_retirar_dinero
from config import TASA_IVA, UMBRAL_RETIRO

def test_calcular_precio_con_iva():
    assert calcular_precio_con_iva(100) == round(100 * (1 + TASA_IVA), 2)

def test_puede_retirar_dinero_dentro_del_umbral():
    assert puede_retirar_dinero(500) is True

def test_puede_retirar_dinero_excede_el_umbral():
    assert puede_retirar_dinero(UMBRAL_RETIRO + 1) is False
