# operaciones.py

from config import TASA_IVA, UMBRAL_RETIRO

def calcular_precio_con_iva(precio_base):
    return round(precio_base * (1 + TASA_IVA), 2)

def puede_retirar_dinero(cantidad):
    return cantidad <= UMBRAL_RETIRO
