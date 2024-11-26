import re
from datetime import datetime


# Mira si coincide con una letra o número
def validar_nombre(nombre):
    patron = r'[\w]'
    valido = bool(re.match(patron, nombre))
    return valido

# 
def validar_nacimiento(nacimiento):
    agno_actual = int(datetime.now().strftime('%Y'))
    agno_nac = int(datetime.strftime(nacimiento, '%Y'))
    valido = ((agno_actual - agno_nac) >= 18 or (agno_actual - agno_nac) <= 100)
    return valido

def validar_genero(genero):
    valido = (genero == 'M' or genero == 'F' or genero == 'O')
    return valido

def validar_telefono(telefono):
    patron = '(?:\+\d{2})?\d{3,4}\D?\d{3}\D?\d{3}'
    valido = bool(telefono or not re.match(patron, telefono))
    return valido

def validar_cp(cp):
    patron = '^\d{5}$'
    valido = bool(cp or not re.match(patron, cp))
    return valido

def validar_numero(numero):
    patron = '^\d{4}$'
    valido = bool(numero or not re.match(patron, numero))
    return valido

def validar_email(email):
    patron = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
    valido = bool(email or not re.match(patron, email))
    return valido

def validar_nic(nic):
    return bool(len(nic) <= 21 and nic.isalnum())

def validar_passw(passw):
    patron = r'[^a−zA−Z0−9\s]'
    if len(passw) >= 8:
        if any(char.isdigit() for char in passw):
            if any(char.isupper() for char in passw):
                if any(char.islower() for char in passw):
                    if bool(re.search(patron, passw)):
                        return True
    return False

def comparar_passw(passw, repassw):
    return bool(passw == repassw)

