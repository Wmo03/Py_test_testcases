# test_clima.py

import pytest
import clima
from unittest.mock import patch

def test_clima_mockeado_valido():
    with patch('clima.obtener_clima_actual', return_value=22):
        clima_resultado = clima.obtener_clima_actual()
        print(f"Clima: {clima_resultado:.1f} celsius")
        assert clima_resultado == 22

def test_clima_mockeado_timeout():
    with patch('clima.obtener_clima_actual', side_effect=TimeoutError("Tiempo agotado")):
        with pytest.raises(TimeoutError) as exc_info:
            clima.obtener_clima_actual()  # aquí ocurre el error
        print(f"[✓ Capturado] → {exc_info.value}")  # ahora sí está disponible
        assert "Tiempo agotado" in str(exc_info.value)



def test_clima_mockeado_error_generico():
    with patch('clima.obtener_clima_actual', side_effect=ValueError("Error en datos de clima")):
        with pytest.raises(ValueError) as exc_info:
            clima.obtener_clima_actual()
            print(f"Error: {exc_info.value}")
        assert "Error en datos de clima" in str(exc_info.value)

def test_clima_respuestas_en_cadena():
    respuestas = [22, 23, 24]
    with patch('clima.obtener_clima_actual', side_effect=respuestas):
        print(f"Valores simulados: {respuestas}")
        assert clima.obtener_clima_actual() == 22
        assert clima.obtener_clima_actual() == 23
        assert clima.obtener_clima_actual() == 24

