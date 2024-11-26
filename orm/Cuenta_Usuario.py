from ..models import Persistencia as mydb
from Usuario import db
import Jardinero
import Propietario

tabla = 'Cuenta_Usuario'

class Cuenta_Usuario:
    def __init__(self, email=str, nic=str, clave=str):
        self.email = email
        self.nic = nic
        self.clave = clave

    def procesar_usuario(usuario=object):
        if isinstance(usuario, Jardinero):
            
            pass
        elif isinstance(usuario, Propietario):
            pass

    def crear_cuenta_usuario(self):
        db.insert(tabla,[self.email, self.nic, self.clave])