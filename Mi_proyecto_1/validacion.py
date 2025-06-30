# validacion.py

import re

def es_email_valido(email):
    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(patron, email) is not None
