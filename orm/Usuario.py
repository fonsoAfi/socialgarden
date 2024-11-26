from ..models import Persistencia as mydb
from abc import ABC, abstractmethod

db = mydb()
tabla = 'Usuario'
usuario_lectura = 'usuario_lectura'
usuario_escritura = 'usuario_escritura'

class Usuario:
    cont = 1
    id_usuario = 0
    def __init__(self, 
                 nombre=None, apellido1=None, apellido2=None, 
                 nacimiento=None, genero=None, descripcion=None, tipo_usuario=None, telefono=None):
        
        self.id_usuario = Usuario.cont
        Usuario.cont += 1
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.nacimiento = nacimiento
        self.genero = genero
        self.descripcion = descripcion
        self.tipo_usuario = tipo_usuario
        self.telefono = telefono


    # Crea el usuario en la Base de Datos con los valores de los atributos
    def crear_usuario(self):
        db.insert(tabla,self.__dict__.values())

    # Getters
    @staticmethod
    def getId():
        return Usuario.id_usuario
    
    def getNombre(self):
        result = db.select(
            columns=[self.nombre],
            table=tabla,
            conditions={'id_usurio':self.id_usuario}
            )
        return result

    def getApellido1(self):
        result = db.select(
            columns=[self.apellido1],
            table=tabla,
            conditions={'id_usurio':self.id_usuario}
            )
        return result

    def getApellido2(self):
        result = db.select(
            columns=[self.apellido2],
            table=tabla,
            conditions={'id_usurio':self.id_usuario}
            )
        return result

    def getNacimiento(self):
        result = db.select(
            columns=[self.nacimiento],
            table=tabla,
            conditions={'id_usurio':self.id_usuario}
            )
        return result

    def getGenero(self):
        db.connect()
        result = db.select(
            columns=[self.genero],
            table=tabla,
            conditions={'id_usurio':self.id_usuario}
            )
        db.disconnect()
        return result

    def getDescripcion(self):
        db.connect()
        result = db.select(
            columns=[self.descripcion],
            table=tabla,
            conditions={'id_usurio':self.id_usuario}
            )
        db.disconnect()
        return result

    def getTipoUsuario(self):
        db.connect()
        result = db.select(
            columns=[self.tipo_usuario],
            table=tabla,
            conditions={'id_usurio':self.id_usuario}
            )
        db.disconnect()
        return result

    def getTelefono(self):
        db.connect()
        result = db.select(
            columns=[self.telefono],
            table=tabla,
            conditions={'id_usurio':self.id_usuario}
            )
        db.disconnect()
        return result

    def getColumns(self):
        db.connect()
        result = db.select(
            columns=['*'],
            table=tabla,
            conditions={'id_usurio':self.id_usuario}
            )
        db.disconnect()
        return result


    # Setters
    def setId(self, id):
        db.connect()
        db.update(
            table=tabla,
            set_values=id,
            conditions={'id_usurio':self.id_usuario}
            )
        db.disconnect()

    def setNombre(self, nombre):
        db.connect()
        db.update(
            table=tabla,
            set_values=nombre,
            conditions={'id_usurio':self.id_usuario}
            )
        db.disconnect()

    def setApellido1(self, apellido1):
        db.connect()
        db.update(
            table=tabla,
            set_values=apellido1,
            conditions={'id_usurio':self.id_usuario}
            )
        db.disconnect()

    def setApellido2(self, apellido2):
        db.connect()
        db.select(
            table=tabla,
            set_values=apellido2,
            conditions={'id_usurio':self.id_usuario}
            )
        db.disconnect()

    def setNacimiento(self, nacimiento):
        db.connect()
        db.select(
            table=tabla,
            set_values=nacimiento,
            conditions={'id_usurio':self.id_usuario}
            )
        db.disconnect()

    def setGenero(self, genero):
        db.connect()
        db.select(
            table=tabla,
            set_values=genero,
            conditions={'id_usurio':self.id_usuario}
            )
        db.disconnect()

    def setDescripcion(self, descripcion):
        db.connect()
        db.select(
            table=tabla,
            set_values=descripcion,
            conditions={'id_usurio':self.id_usuario}
            )
        db.disconnect()

    def setTelefono(self, telefono):
        db.connect()
        db.select(
            table=tabla,
            set_values=telefono,
            conditions={'id_usurio':self.id_usuario}
            )
        db.disconnect()




    