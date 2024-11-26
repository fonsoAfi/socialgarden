import Usuario
from Usuario import db

tabla = 'Propietario'

class Propietario(Usuario):
    """Clase concreta para el tipo de usuario Jardinero."""
    def __init__(self, id_usuario, nombre, apellido1, apellido2, 
                 nacimiento, genero, descripcion, tipo_usuario, telefono,
                 id_propietario=int):
        
        super().__init__(id_usuario, nombre, apellido1, apellido2, 
                         nacimiento, genero, descripcion, tipo_usuario, telefono)
        
        self.id_propietario = id_propietario

    def crear_usuario(self):
        db.insert(tabla,[self.__dict__.values()])

    def obtener_tipo(self):
        return "Propietario"

    def __str__(self):
        base = super().__str__()
        return f"{base}, Experiencia: {self.experiencia}, Especialidad: {self.especialidad}"
