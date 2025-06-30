# test_sistema.py

from sistema import obtener_marca_tiempo
import time

def test_reloj_sistema_avanza_correctamente():
    t1 = obtener_marca_tiempo()
    

    time.sleep(0.2)  # Esperamos 1.5 segundos
    t2 = obtener_marca_tiempo()
    


    # Calculamos cuánto tiempo pasó realmente
    delta = t2 - t1
    print(f"Tiempo transcurrido real: {delta:.4f} segundos")


    # Validamos que haya pasado al menos 1.4 segundos (tolerancia) y no más de 2
    assert 0.1 <= delta <= 0.3, f"El reloj no avanza correctamente, delta={delta:.4f}s"
